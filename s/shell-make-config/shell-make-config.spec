%define _unpackaged_files_terminate_build 1

Name: 	  shell-make-config
Version:  0.1.1
Release:  alt1

Summary:  Makefile-style config file editing shell library
License:  GPLv3
Group:    Development/Other
Url: 	  http://git.altlinux.org/people/manowar/packages/shell-make-config.git

Source:   %name-%version.tar
BuildArch: noarch

%description
shell-make-config provides shell functions to edit
Makefile-style configuration files (like /etc/initrd.mk).

%prep
%setup

%install
install -D -m0644 shell-make-config %buildroot%_bindir/shell-make-config

%files
%_bindir/shell-make-config

%changelog
* Mon Mar 18 2024 Paul Wolneykien <manowar@altlinux.org> 0.1.1-alt1
- Fixed argument checking in the functions.
- Fixed the code as suggested by shellcheck.

* Tue Mar 12 2024 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt1
- Initial version.
