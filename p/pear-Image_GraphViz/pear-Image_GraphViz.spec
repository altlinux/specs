%define pear_name Image_GraphViz

Name: pear-Image_GraphViz
Version: 1.2.1
Release: alt3

Summary: Interface to AT&T's GraphViz tools

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/Image_GraphViz

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Image_GraphViz-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
The GraphViz class allows for the creation of and the work with directed
and undirected graphs and their visualization with AT&T's GraphViz tools.

%prep
%setup -c

%build
%pear_build

%install
%pear_install_std

%post
%register_pear_module

%preun
%unregister_pear_module

%files
%doc LICENSE CHANGELOG
%pear_dir/Image
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt1
- initial build for ALT Linux Sisyphus

