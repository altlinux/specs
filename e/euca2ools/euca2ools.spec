Name: euca2ools
Version: 3.4.1
Release: alt1
Summary: Eucalyptus/AWS-compatible command line tools

Group: Networking/Other
License: BSD
Url: https://github.com/eucalyptus/euca2ools

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python

BuildArch: noarch

%description
Euca2ools are command line tools used to interact with Amazon Web
Services (AWS) as well as other services that are compatible with AWS,
such as Eucalyptus.  They aim to use the same input as similar tools
provided by AWS for each service individually along with several
enhancements that make them easier to use with multiple clouds at once.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc README
%_bindir/eu*
%python_sitelibdir/%{name}*
%_man1dir/eu*
%_man5dir/euca2ools.ini.5*
%_man7dir/euca2ools.7*

%changelog
* Tue Jun 02 2020 Andrey Cherepanov <cas@altlinux.org> 3.4.1-alt1
- New version.

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1-alt1.1
- Rebuild with Python-2.7

* Wed Feb 03 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1-alt1
- Initial

