Name: randomize_fd
Version: 0.1
Release: alt1

Summary: Randomizes the fd returned by open or socket when LD_PRELOADed

BuildRequires(pre): rpm-build-licenses
License: %lgpl3plus
Group: Development/Debuggers
Url: http://git.altlinux.org/people/imz/packages/randomize_fd.git

Source: %name-%version.tar

BuildRequires: gcc
# due to mkdir implied by install -D -t
BuildPreReq: coreutils >= 8.27

%description
Sometimes (to reproduce a bug) we want to force the use of different
file descriptors in a sequence of open(2) or socket(2) followed by
`close`, so that:

1. the new fd is different from the previous one,
2. and the previous one doesn't look like a valid descriptor anymore.

Here, we solve this problem by providing wrappers around open(2) and
socket(2) to be LD_PRELOADed.

%prep
%setup

%build
%make_build

%install
install -m0644 -D *.so -t %buildroot%_libdir
ln -sfv /usr/share/license/LGPL-3 -T COPYING

%files
%_libdir/*.so
%doc README.md TODO.md COPYING

%changelog
* Mon Mar 12 2018 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt1
- Initial build for ALT Sisyphus.


