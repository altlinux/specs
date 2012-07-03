%define pear_name XML_RPC2

Name: pear-XML_RPC2
Version: 1.0.2
Release: alt3

Summary: XML-RPC client/server library

License: LGPL
Group: Development/Other
Url: http://pear.php.net/package/XML_RPC2

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/XML_RPC2-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: pear-Cache_Lite >= 1.6.0

%description
XML_RPC2 is a pear package providing XML_RPC client and server services.
XML-RPC is a simple remote procedure call protocol built using HTTP as
transport and XML as encoding.
As a client library, XML_RPC2 is capable of creating a proxy class which
exposes the methods exported by the server. As a server library, XML_RPC2
is capable of exposing methods from a class or object instance, seamlessly
exporting local methods as remotely callable procedures.

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
%pear_testdir/XML_RPC2/
%pear_dir/XML/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt1
- initial build for ALT Linux Sisyphus

