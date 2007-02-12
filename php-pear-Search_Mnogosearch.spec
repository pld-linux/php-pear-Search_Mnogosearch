%include	/usr/lib/rpm/macros.php
%define		_class		Search
%define		_subclass	Mnogosearch
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - Wrapper classes for the mnoGoSearch extention
Summary(pl.UTF-8):	%{_pearname} - Klasy do obsługi rozszerzenia mnoGoSearch
Name:		php-pear-%{_pearname}
Version:	0.1.1
Release:	5
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	af6c5903821f72e00c65dc573e638581
URL:		http://pear.php.net/package/Search_Mnogosearch/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(mnogosearch)
Requires:	php-common >= 3:5.0.0
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	'pear(HTML/QuickForm.*)' 'pear(HTML/Template/Sigma.*)' 'pear(Pager.*)'

%description
This package provides wrapper classes for the mnoGoSearch search
engine. The package has two central classes "Search_Mnogosearch" and
"Search_Mnogosearch_Result". The class "Search_Mnogosearch" gives an
object that represents the search and the "Search_Mnogosearch_Result"
the result. The usage is just like the usage in the "DB" and
"DB_result" classes.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ten pakiet dostarcza klasy obudowujące dla silnika wyszukiwarki
mnoGoSearch. Pakiet ma dwie główne klasy: Search_Mnogosearch i
Search_Mnogosearch_Result. Klasa Search_Mnogosearch daje obiekt
reprezentujący wyszukiwanie, a Search_Mnogosearch_Result - wynik.
Sposób użycia jest podobny do klas DB i DB_result.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%dir %{php_pear_dir}/%{_class}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
