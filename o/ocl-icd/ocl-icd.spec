Name: ocl-icd
Version: 2.3.2
Release: alt1

Summary: OpenCL ICD Bindings

License: BSD
Group: Development/C
Url: https://github.com/OCL-dev/ocl-icd

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/OCL-dev/ocl-icd/archive/v%version.tar.gz
Source: %name-%version.tar

BuildRequires: opencl-headers
# for code generator
BuildRequires: ruby rubygems

# for man
BuildRequires: asciidoc asciidoc-a2x xmlto

#Recommends:     beignet
#Recommends:     mesa-libOpenCL
#Recommends:     pocl

%description
%summary.

%package devel
Summary: Development files for %name
Requires: %name = %version-%release
Requires: opencl-headers
Group: Development/C

%description devel
This package contains the development files for %name.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
rm -vf %buildroot%_libdir/*.la
rm -vrf %buildroot%_docdir

%check
make check

%files
%doc COPYING
%doc NEWS README
%_libdir/libOpenCL.so.*

%files devel
%doc ocl_icd_loader_gen.map ocl_icd_bindings.c
%_bindir/cllayerinfo
%_includedir/ocl_icd.h
%_libdir/libOpenCL.so
%_pkgconfigdir/%name.pc
%_pkgconfigdir/OpenCL.pc
%_man7dir/*

%changelog
* Sun Dec 03 2023 L.A. Kostis <lakostis@altlinux.ru> 2.3.2-alt1
- Updated to v2.3.2 (Fix FTBFS with new opencl-headers).
- Added cllayerinfo to -devel subpackage.

* Sun Feb 28 2021 Vitaly Lipatov <lav@altlinux.ru> 2.2.14-alt1
- new version 2.2.14 (with rpmrb script)
- change source url and url

* Sat Jun 09 2018 Vitaly Lipatov <lav@altlinux.ru> 2.2.12-alt1
- new version 2.2.12 (with rpmrb script)

* Sat Jun 17 2017 Vitaly Lipatov <lav@altlinux.ru> 2.2.11-alt1
- initial build for ALT Sisyphus

* Thu Feb 09 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.2.11-2
- Add Recommends for all OpenCL implementations

* Fri Jan 20 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.2.11-1
- Update to 2.2.11 (RHBZ #1415150)

* Sun Dec 04 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.2.10-1
- Update to 2.2.10

* Mon Nov 21 2016 Orion Poplawski <orion@cora.nwra.com> - 2.2.9-3
- Drop unneeded BR on rubypick

* Wed Aug 31 2016 Igor Gnatenko <ignatenko@redhat.com> - 2.2.9-2
- Rebuild for OpenCL 2.1

* Sun Aug 14 2016 Igor Gnatenko <ignatenko@redhat.com> - 2.2.9-1
- Update to 2.2.9
- Drop requires for opencl-icd

* Fri Apr 08 2016 Björn Esser <fedora@besser82.io> - 2.2.8-3.git20151217.0122332
- add Requires for virtual Provides: opencl-icd (RHBZ #1317600)
- add rubygems and rubypick to BuildRequires

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.8-2.git20151217.0122332
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 21 2015 François Cami <fcami@fedoraproject.org> - 2.2.8-1.git20151217.0122332
- Update to 2.2.8.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.7-2.git20150606.ebbc4c1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 09 2015 François Cami <fcami@fedoraproject.org> - 2.2.7-1.git20150609.ebbc4c1
- Update to 2.2.7.

* Sun Jun 07 2015 François Cami <fcami@fedoraproject.org> - 2.2.5-1.git20150606.de64dec
- Update to 2.2.5 (de64dec).

* Mon May 18 2015 Fabian Deutsch <fabiand@fedorproject.org> - 2.2.4-1.git20150518.7c94f4a
- Update to 2.2.4 (7c94f4a)

* Mon Jan 05 2015 François Cami <fcami@fedoraproject.org> - 2.2.3-1.git20141005.7cd0c2f
- Update to 2.2.3 (7cd0c2f).

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-3.git20131001.4ee231e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-2.git20131001.4ee231e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Oct 01 2013 Björn Esser <bjoern.esser@gmail.com> - 2.0.4-1.git20131001.4ee231e
- update to recent git-snapshot
- general cleanup, squashed unneeded BuildRequires
- cleanup the %%doc mess.
- add %%check for running the testsuite

* Wed Aug 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-3
- Specfile cleanup

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 08 2013 Rob Clark <rclark@redhat.com> 2.0.2-1
- ocl-icd 2.0.2
