%define rname qtruby

Name: ruby-qt4
Version: 4.14.0
Release: alt4

Group: Development/Ruby
Summary: QtRuby kdebindings library
Url: https://projects.kde.org/projects/kde/kdebindings/ruby/qtruby
License: LGPL-2.1+

Source: %rname-%version.tar
# Automatically added by buildreq on Wed Aug 20 2014 (-bi)
# optimized out: cmake-modules elfutils fontconfig libcloog-isl4 libgst-plugins libqscintilla2-11-qt4 libqt4-core libqt4-dbus libqt4-declarative libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-sql libqt4-sql-sqlite libqt4-svg libqt4-test libqt4-uitools libqt4-webkit libqt4-xml libqt4-xmlpatterns libstdc++-devel python-base rpm-build-ruby ruby ruby-stdlibs smokegen-devel
#BuildRequires: cmake gcc-c++ libqscintilla2-qt4-devel libqt3-devel libqwt-devel libruby-devel phonon-devel python-module-protobuf qt4-designer smokeqt-devel
BuildRequires: cmake gcc-c++ libqscintilla2-qt4-devel libqwt-devel libruby-devel phonon-devel smokegen-devel smokeqt-devel
BuildRequires: libsqlite3-devel libqt4-devel kde-common-devel

%filter_from_requires /^ruby(qtruby)/d

%description
Ruby bindings for the Qt4 libraries from the kdebindings project.

%package devel
Summary: Development libraries for Ruby-Qt4
Group: Development/Ruby
Requires: %name = %version
%description devel
This package contains development files for the Ruby bindings for the Qt4 libraries.

%package -n libqtruby4
Summary: %name library
Group: System/Libraries
#Requires: %name-common = %version-%release
%description -n libqtruby4
%name library

%prep
%setup -n %rname-%version

%build
%K4build

%install
%K4install

# add missing executable bits on scripts
chmod +x %buildroot/%ruby_sitelibdir/qwt/qwt.rb
chmod +x %buildroot/%ruby_sitelibdir/qtdeclarative/qtdeclarative.rb
chmod +x %buildroot/%ruby_sitelibdir/phonon/phonon.rb
chmod +x %buildroot/%ruby_sitelibdir/qscintilla/qscintilla.rb
chmod +x %buildroot/%ruby_sitelibdir/qtuitools/qtuitools.rb
chmod +x %buildroot/%ruby_sitelibdir/qtwebkit/qtwebkit.rb

%files -n libqtruby4
%_K4libdir/libqtruby4shared.so.*

%files
%_K4bindir/rbqtapi
%_K4bindir/rbrcc
%_K4bindir/rbuic4
%ruby_sitelibdir/*.rb
%ruby_sitelibdir/Qt/
%ruby_sitelibdir/phonon/
%ruby_sitelibdir/qtdeclarative/
%ruby_sitelibdir/qtscript/
%ruby_sitelibdir/qttest/
%ruby_sitelibdir/qtuitools/
%ruby_sitelibdir/qtwebkit/
%ruby_sitelibdir/qscintilla/
%ruby_sitelibdir/qwt/
%ruby_sitearchdir/*.so

%files devel
%_K4link/libqtruby4shared.so
%_includedir/qtruby/
%_datadir/qtruby4/

%changelog
* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 4.14.0-alt4
- Rebuild with new %%ruby_sitearchdir location

* Fri Sep 23 2016 Sergey V Turchin <zerg@altlinux.org> 4.14.0-alt3
- rebuild with new libruby

* Fri Oct 16 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.0-alt2
- rebuild with gcc5

* Wed Aug 20 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.0-alt1
- initial build
