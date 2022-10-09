%define pkg qemu

Name: rpm-macros-%pkg
Version: 0.2
Release: alt1

Summary: Arch macro to build %pkg clients
License: MIT
Group: Development/Other

Url: http://altlinux.org/ports
Source: macros
BuildArch: noarch

%description
%pkg supports only some architectures.

This package provides a macro with the list of architectures
supported by %pkg in ALT Linux.

%install
install -pDm644 %SOURCE0 %buildroot%_rpmmacrosdir/%pkg

%files
%_rpmmacrosdir/%pkg

%changelog
* Sun Oct 09 2022 Michael Shigorin <mike@altlinux.org> 0.2-alt1
- added %%qemu_check

* Sun Oct 09 2022 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release (generalized off rpm-macros-luajit 0.3-alt1)
