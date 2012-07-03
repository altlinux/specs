Name: installer-feature-xCAT-stage3
Version: 0.1
Release: alt4

%define hookpostdir %_datadir/install2/postinstall.d

Packager:  Andriy Stepanov <stanv@altlinux.ru>
Summary:   ALT Linux installer part, setup xCAT compute node settings
Group:     System/Configuration/Other
License:   GPL
Url:       http://www.altlinux.org/Installer/beans
BuildArch: noarch
Source1:   81-xCAT-postinstall.sh

%description
Contains installer stage3 hook to setup
compute node settings according to managment node parameters.

%prep

%install
mkdir -p %buildroot%hookpostdir
install -pm755 %SOURCE1 %buildroot%hookpostdir/

%files
%hookpostdir/*

%changelog
* Mon Jan 25 2010 Andriy Stepanov <stanv@altlinux.ru> 0.1-alt4
- Don't include twice install2 functions

* Wed Jan 20 2010 Andriy Stepanov <stanv@altlinux.ru> 0.1-alt3
- use `cmdline_has_arg'

* Wed Jan 20 2010 Andriy Stepanov <stanv@altlinux.ru> 0.1-alt2
- parse cmdline

* Wed Jan 20 2010 Andriy Stepanov <stanv@altlinux.ru> 0.1-alt1
- Initial package.
