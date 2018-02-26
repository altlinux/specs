%define pear_name Net_URL2
Name: pear-%pear_name
Version: 0.3.1
Release: alt1

Summary: Class for parsing and handling URL

License: BSD
Group: Development/Other
Url: http://pear.php.net/package/%pear_name

Source: http://pear.php.net/get/%pear_name-%version.tar

BuildArch: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
Provides parsing of URLs into their constituent parts (scheme, host, path etc.),
URL generation, and resolving of relative URLs.

%prep
%setup -c -n %pear_name-%version

%build
%pear_build

%install
%pear_install_std


%post
%register_pear_module

%preun
%unregister_pear_module


%files
%pear_dir/Net/
%pear_xmldir/%pear_name.xml
%pear_docdir/%pear_name/

%changelog
* Sat Oct 23 2010 Vitaly Lipatov <lav@altlinux.ru> 0.3.1-alt1
- initial build for ALT Linux Sisyphus

