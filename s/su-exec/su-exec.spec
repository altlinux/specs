Name:     su-exec
Version:  0.2
Release:  alt1

Summary:  switch user and group id and exec
License:  MIT
Group:    Other
Url:      https://github.com/ncopa/su-exec

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source:   %name-%version.tar

%description
This is a simple tool that will simply execute a program with different
privileges. The program will be exceuted directly and not run as a child, like
su and sudo does, which avoids TTY and signal issues.

Notice that su-exec depends on being run by the root user, non-root users do
not have permission to change uid/gid.

%prep
%setup

%build
%make_build

%install
install -D su-exec -t %buildroot%_bindir

%files
%_bindir/*
%doc *.md

%changelog
* Fri Feb 15 2019 Mikhail Gordeev <obirvalger@altlinux.org> 0.2-alt1
- Initial build for Sisyphus
