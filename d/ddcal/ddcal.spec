Name: ddcal
Version: 0.9
Release: alt5
Summary: BDD calculator based on CUDD
License: BSD
Group: Sciences/Mathematics
Url: http://vlsi.colorado.edu/vlsi_downloads.html
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-make
BuildPreReq: graphviz perl-Tk libcudd-devel flex

Requires: perl-Tk

%description
DDcal is a BDD calculator based on perl-Tk and the Cudd package.

%prep
%setup

%build
%add_optflags -I%_includedir/cudd
%make_build_ext

%install
%makeinstall_std

mv %buildroot%_bindir/%name %buildroot%_bindir/%name.bin
cat <<EOF >%buildroot%_bindir/%name
#!/bin/sh

%_bindir/DDcal -program %_bindir/ddcal.bin
EOF
chmod +x %buildroot%_bindir/%name

%files
%doc README examples
%_bindir/*

%changelog
* Thu Dec 10 2020 Vladislav Zavjalov <slazav@altlinux.org> 0.9-alt5
- fix multiple definition error (for gcc-10)

* Thu Oct 03 2019 Vladislav Zavjalov <slazav@altlinux.org> 0.9-alt4
- fix building

* Tue Sep 04 2018 Vladislav Zavjalov <slazav@altlinux.org> 0.9-alt3
- fix building

* Sun Aug 12 2018 Vladislav Zavjalov <slazav@altlinux.org> 0.9-alt2
- fix building with make -jN

* Mon Mar 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1
- Initial build for Sisyphus

