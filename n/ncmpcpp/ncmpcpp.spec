%define _unpackaged_files_terminate_build 1

%define libquadmath_arches %ix86 x86_64 ppc64le

Name: ncmpcpp
Version: 0.9.2
Release: alt1

Summary: ncurses-based client for the Music Player Daemon (MPD)

Group: Sound
License: GPLv2+
URL: https://rybczak.net/ncmpcpp/

VCS: https://github.com/ncmpcpp/ncmpcpp.git
Source: %name-%version.tar
# git://git.altlinux.org/gears/n/ncmpcpp.git
Patch1: %name-%version-%release.patch

# Automatically added by buildreq on Fri Jul 28 2017
# optimized out: boost-devel boost-devel-headers glibc-kernheaders-x86 libncurses-devel libstdc++-devel libtinfo-devel perl pkg-config python-base python3 python3-base
BuildRequires: boost-filesystem-devel boost-locale-devel boost-program_options-devel gcc-c++ glibc-devel-static glibc-kernheaders-generic libcurl-devel libfftw3-devel libmpdclient-devel libncursesw-devel libreadline-devel libtag-devel python3-dev
%ifarch %libquadmath_arches
BuildRequires: libquadmath-devel
%endif

%description
ncmpcpp is almost an exact clone of ncmpc which is a text-mode client
for MPD, the Music Player Daemon. It provides a keyboard oriented and
consistent interface to MPD and contains some new features ncmpc
doesn't have. It's been also rewritten from scratch in C++.

%prep
%setup
%patch1 -p1

%build
%autoreconf
%configure \
    --enable-clock \
    --enable-outputs \
    --enable-visualizer \
    --with-fftw \
    --with-taglib \
    #
%make_build

%install
%makeinstall_std
mv %buildroot%_docdir/%name percentDoc

%files
%doc percentDoc/*
%_bindir/%name
%_man1dir/%name.1*

%changelog
* Thu Dec 16 2021 Arseny Maslennikov <arseny@altlinux.org> 0.9.2-alt1
- 0.9.1 -> 0.9.2.

* Tue Jan 05 2021 Arseny Maslennikov <arseny@altlinux.org> 0.9.1-alt1
- 0.8.1 -> 0.9.1.
- Restore the package for aarch64.

* Tue Dec 03 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.1-alt2
- Excluded from aarch64 and rebuilt with new boost-1.71.0.

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.1-alt1.1
- NMU: rebuilt with boost-1.67.0

* Sun Nov 12 2017 Arseny Maslennikov <arseny@altlinux.org> 0.8.1-alt1
- 0.8.1-alt1
- Update .gitignore

* Wed Oct 11 2017 Arseny Maslennikov <arseny@altlinux.org> 0.8-alt2
- Rebuilt with libboost_*.so.1.65.0

* Fri Jul 28 2017 Arseny Maslennikov <arseny@altlinux.org> 0.8-alt1
- Initial build for ALT Sisyphus

