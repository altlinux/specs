# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Name: animorph
Version: 0.3
Release: alt3
Summary: 3D Animation and Morph Library

Group: System/Libraries
License: GPLv3+
Url: http://www.makehuman.org
Source0: http://downloads.sourceforge.net/makehuman/%name-%version.tar.gz

Packager: Ilya Mashkin <oddity@altlinux.ru>
Patch0: animorph-0.2-pkgconfig.patch
Patch1: animorph-0.3-gcc43.patch
Patch2: animorph-0.3-gcc44.patch
Source44: import.info

%description
3D Animation and Morph Library

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup
# We need to fix CRLF first
for f in animorph*.in AUTHORS COPYING TODO; do
  sed -i 's/\r//' $f
  touch -r README $f
done
%patch0 -p1 -b .pkgconfig
%patch1 -p1 -b .gcc43
%patch2 -p1 -b .gcc44

# prevent timestramps changes from patch1
pushd include/animorph
for f in util.h BodySettings.h FaceGroup.h Hotspot.h;do
touch -r $f.gcc43 $f
done
popd

%build
export CXXFLAGS="$RPM_OPT_FLAGS -std=c++0x"
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p -c"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

# Removes doc
rm -rf $RPM_BUILD_ROOT%prefix/doc

%files
%doc AUTHORS TODO
%_libdir/*.so.*

%files devel
%_includedir/%name/
%_libdir/*.so
%_libdir/pkgconfig/%name.pc

%changelog
* Wed Mar 19 2014 Ilya Mashkin <oddity@altlinux.ru> 0.3-alt3
- Build for Sisyphus

* Thu Aug 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.3-alt2_12
- update to new release by fcimport

* Thu Feb 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.3-alt2_11
- update to new release by fcimport

* Thu Aug 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.3-alt2_10
- update to new release by fcimport

* Tue May 22 2012 Igor Vlasenko <viy@altlinux.ru> 0.3-alt2_9
- regenerated with 0.46 R::S::C

* Fri May 18 2012 Igor Vlasenko <viy@altlinux.ru> 0.3-alt1_9
- converted for Sisyphus

