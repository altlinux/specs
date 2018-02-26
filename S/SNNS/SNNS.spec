Name: SNNS
Version: 4.3
Release: alt1.1.1.1
Summary: Stuttgart Neural Network Simulator

%define vname %{name}v%version

Group: Sciences/Computer science
License: LGPL
Url: http://www.ra.cs.uni-tuebingen.de/SNNS
Source0: http://www.ra.cs.uni-tuebingen.de/downloads/SNNS/SNNSv%version.tar.gz
Patch0: SNNSv4.3.diff
Patch1: SNNS-sprintf-alt.patch
Packager: Fr. Br. George <george@altlinux.ru>

# Automatically added by buildreq on Thu Oct 08 2009
BuildRequires: flex imake libXaw3d-devel libXext-devel libXmu-devel makedepend python-devel xorg-cf-files

%description
SNNS (Stuttgart Neural Network Simulator) is a software simulator for neural
networks on Unix workstations developed at the Institute for Parallel and
Distributed High Performance Systems (IPVR) at the University of Stuttgart.
The goal of the SNNS project is to create an efficient and flexible
simulation environment for research on and application of neural nets.

%setup_python_module %name
%package -n %packagename
Group:		Development/Python
License:	LGPL
Summary:	Python bingings for Stuttgart Neural Network Simulator

%description -n %packagename
This is a Python module that provides the SNNS kernel functions.
This should allow much better scripting than batchman and could be a
first step towards a replacement GUI (for example using Tkinter).

%prep
%setup -q -n %{name}v%version
%patch0 -p1
%patch1 -p1
# binaries inside of tarball
rm -rf */bin/*
# Fedora's Xaw3d headers are in X11/Xaw3d, not in X11/Xaw
sed -i -e 's,X11/Xaw/,X11/Xaw3d/,g' xgui/sources/*.c

%build
%configure --enable-global
%make_build compile
( cd tools/doc; for N in *.doc; do cp $N ../bin/${N%%%%.doc}.txt; done )
( cd python; %python_build )

%install
mkdir -p %buildroot%_bindir %buildroot%_mandir
make install INSTALLDIR=%buildroot%prefix
make install-man INSTALLDIR=%buildroot
install -D help.hdoc %buildroot%_datadir/%vname/help.hdoc
cp -a examples %buildroot%_datadir/%vname
install -D default.cfg %buildroot%_sysconfdir/%vname/default.cfg
ln -s xgui %buildroot%_bindir/snns
( cd python; %python_install )

%files
%doc Readme.license tools/bin/*
%_bindir/*
%_man1dir/*
%_datadir/%vname
%_sysconfdir/%vname

%files -n %packagename
%doc python/README python/examples
%python_sitelibdir/snns
%python_sitelibdir/snns/*

%changelog
* Mon Apr 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 4.3-alt1.1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.3-alt1.1.1
- Rebuild with Python-2.7

* Wed Nov 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3-alt1.1
- Rebuilt with python 2.6

* Thu Oct 08 2009 Fr. Br. George <george@altlinux.ru> 4.3-alt1
- Initial build from FC
- python module provided

* Fri Mar 20 2009	Ralf Corsépius <corsepiu@fedoraproject.org> - 4.3-2
- Various fixes.

* Thu Mar 19 2009	Ralf Corsépius <corsepiu@fedoraproject.org> - 4.3-1
- Initial Fedora package.
