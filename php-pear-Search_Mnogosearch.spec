%define		_status		alpha
%define		_pearname Search_Mnogosearch
Summary:	%{_pearname} - Wrapper classes for the mnoGoSearch extention
Summary(pl.UTF-8):	%{_pearname} - Klasy do obsługi rozszerzenia mnoGoSearch
Name:		php-pear-%{_pearname}
Version:	0.1.1
Release:	8
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	af6c5903821f72e00c65dc573e638581
URL:		http://pear.php.net/package/Search_Mnogosearch/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.654
Requires:	php(core) >= 5.0.0
Requires:	php-mnogosearch
Requires:	php-pear
Suggests:	php-pear-HTML_QuickForm >= 3.2.3
Suggests:	php-pear-HTML_Template_Sigma >= 1.1.1
Suggests:	php-pear-Pager >= 2.2.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq_pear HTML/QuickForm.* HTML/Template/Sigma.* Pager.*

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
%dir %{php_pear_dir}/Search
%{php_pear_dir}/Search/*.php
%{php_pear_dir}/Search/Mnogosearch
