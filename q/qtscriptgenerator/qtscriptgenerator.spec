%define qt4_ver %{get_version libqt4-devel}

Name: qtscriptgenerator
Version: 0.1.0
Release: alt3

Group: Development/KDE and QT
Summary: Qt bindings for Qt Script
License: GPLv2
Url: http://code.google.com/p/qtscriptgenerator/

Requires: qtscriptbindings = %{version}-%{release}

Source: %name-src-%version.tar.gz
# MDK
Patch2: qtscriptgenerator-src-0.1.0-fix-build.patch
Patch3: qtscriptgenerator-src-0.1.0-fix-strings.patch
# RH
Patch50: qtscriptgenerator-0.1.0-gcc44.patch
Patch51: memory_alignment_fix.diff
Patch52: qtscriptgenerator-kde_phonon443.patch
Patch53: qtscriptgenerator-src-0.1.0-no_QFileOpenEvent.patch
Patch54: qtscriptgenerator-src-0.1.0-qmake_target.path.patch

BuildRequires(pre): libqt4-devel kde-common-devel
BuildRequires: gcc-c++ phonon-devel xsltproc

%description
The Qt Script Generator is a tool that generates Qt bindings for Qt Script.
Qt Script Generator is a tool that generates Qt bindings for Qt Script.
With the generated bindings you get access to substantial portions of 
the Qt API from within Qt Script.

%package -n qtscriptbindings
Summary: Qt bindings for Qt Script
Group: System/Libraries
Provides: qtscript-qt = %version-%release
%description -n qtscriptbindings
Bindings providing access to substantial portions of the Qt API
from within Qt Script.


%prep
%setup -q -n %name-src-%version
%patch2 -p0
%patch3 -p1
%patch50 -p0
%patch51 -p1
%patch52 -p1
%_K_if_ver_gteq %qt4_ver 4.8
%patch53 -p1
%endif
%patch54 -p1

cat >>qtbindings/qtbindingsbase.pri <<__EOF__
CONFIG -= debug_ang_release
CONFIG += release
QMAKE_CXXFLAGS += \$(RPM_OPT_FLAGS)
__EOF__
cat >>generator/generator.pri <<__EOF__
CONFIG -= debug_ang_release
CONFIG += release
QMAKE_CXXFLAGS += \$(RPM_OPT_FLAGS)
__EOF__
cat >>tools/qsexec/src/qsexec.pro <<__EOF__
CONFIG -= debug_ang_release
CONFIG += release
QMAKE_CXXFLAGS += \$(RPM_OPT_FLAGS)
__EOF__
pushd generator
qmake-qt4
popd
pushd qtbindings
qmake-qt4
popd
pushd tools/qsexec/src
qmake-qt4
popd


%build
export QTDIR="" INCLUDE=%_includedir/qt4
pushd generator
%make 
./generator
popd

pushd qtbindings
%make_build
popd

pushd tools/qsexec/src
%make_build
popd


%install
mkdir -p  %buildroot/%_qt4dir/plugins/script/
cp -a plugins/script/libqtscript* \
  %buildroot/%_qt4dir/plugins/script/
install -D -p -m0755 tools/qsexec/qsexec %buildroot/%_bindir/qsexec
install -D -p -m0755 generator/generator %buildroot/%_qt4dir/bin/generator
cp -a tools/qsexec/README.TXT README.qsexec


%files
%_qt4dir/bin/generator

%files -n qtscriptbindings
%doc README README.qsexec
%doc doc/
%doc examples/
%_bindir/qsexec
%_qt4dir/plugins/script/libqtscript*

%changelog
* Tue Jan 24 2012 Sergey V Turchin <zerg@altlinux.org> 0.1.0-alt3
- fix to build with qt-4.8

* Wed Mar 02 2011 Sergey V Turchin <zerg@altlinux.org> 0.1.0-alt2
- rebuilt

* Fri Jun 05 2009 Sergey V Turchin <zerg@altlinux.org> 0.1.0-alt0.M50.1
- built for M50

* Wed Apr 15 2009 Sergey V Turchin <zerg@altlinux.org> 0.1.0-alt1
- initial specfile

