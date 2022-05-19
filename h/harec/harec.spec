Name:           harec
Version:        2022.05.17
Release:        alt1
Group:          Development/Other
Source:         %name-%version.tar
URL:            https://git.sr.ht/~sircmpwn/harec
Summary:        Hare language compiler written in C11 for POSIX-compatible systems.
License:        GPLv3
ExclusiveArch:  x86_64 aarch64
# git clone     https://git.sr.ht/~sircmpwn/harec
# cd harec; git archive --prefix=harec-`git log -1 --format='%as' | tr - .`/ --output=../RPM/SOURCES/harec-`git log -1 --format='%as' | tr - .`.tar HEAD


# Automatically added by buildreq on Thu May 19 2022
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 libgpg-error python3-base sh4
BuildRequires: python3 qbe

%description
Harec includes a minimal runtime under rt which is suitable for running
the test suite, but not recommended for production use. See
docs/runtime.txt for details on how to provide your own runtime
implementation, or use the Hare standard library.

%prep
%setup

%build
./configure
%make PREFIX=%_prefix

%install
%makeinstall_std PREFIX=%_prefix DESTDIR=%buildroot

%files
%doc *.md
%_bindir/*

%check
make check

%changelog
* Thu May 19 2022 Fr. Br. George <george@altlinux.org> 2022.05.17-alt1
- Initial build for ALT
