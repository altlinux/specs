%define pear_name System_Command

Name: pear-System_Command
Version: 1.0.6
Release: alt3

Summary: PEAR::System_Command is a commandline execution interface

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/System_Command

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/System_Command-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
System_Command is a commandline execution interface. Running functions from
the commandline can be risky if the proper precautions are not taken to
escape the shell arguments and reaping the exit status properly. This class
provides a formal interface to both, so that you can run a system command
as comfortably as you would run a php function, with full pear error
handling as results on failure. It is important to note that this class,
unlike other implementations, distinguishes between output to stderr and
output to stdout. It also reports the exit status of the command. So in
every sense of the word, it gives php shell capabilities.

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
%pear_dir/System
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.6-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.6-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.6-alt1
- initial build for ALT Linux Sisyphus

