Name: man-sh
Version: 0.1.2
Release: alt1

Summary: Program to format and display the manual pages (shell implementation)
License: GPL3
Group: System/Servers
BuildArch: noarch

Packager: Alexey Gladkov <legion@altlinux.ru>

Source0: %name-%version.tar

%description
man formats and displays the manual pages.

%prep
%setup -q

%build
%make_build

%install
%makeinstall
install -D -m644 mansh.completion %buildroot%_sysconfdir/bash_completion.d/%name
rm -f -- %buildroot%_sysconfdir/*.conf

%files
%_bindir/*
%_sysconfdir/bash_completion.d/%name

%changelog
* Fri Aug 28 2009 Alexey Gladkov <legion@altlinux.ru> 0.1.2-alt1
- Fix -C option;
- man-sh-functions: Fix directories order;
- Use MAN_CONFIG variable.

* Wed Aug 19 2009 Alexey Gladkov <legion@altlinux.ru> 0.1.1-alt1
- Code optimization.

* Mon Aug 17 2009 Alexey Gladkov <legion@altlinux.ru> 0.1.0-alt1
- First build.
