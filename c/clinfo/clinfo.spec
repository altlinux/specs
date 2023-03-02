Name: clinfo
Version: 3.0.23.01.25
Release: alt1

Summary: Enumerate OpenCL platforms and devices

License: CC0
Group: File tools
Url: https://github.com/Oblomov/clinfo

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/Oblomov/clinfo/archive/%version/%name-%version.tar.gz
Source: %name-%version.tar

BuildRequires: ocl-icd-devel

%description
A simple OpenCL application that enumerates all possible platform and
device properties. Inspired by AMD's program of the same name, it is
coded in pure C99 and it tries to output all possible information,
including that provided by platform-specific extensions, and not to
crash on platform-unsupported properties (e.g. 1.2 properties on 1.1
platforms).

%prep
%setup

%build
export CFLAGS="%optflags"
#export LDFLAGS=""
%make_build

%install
install -Dpm0755 %name %buildroot%_bindir/%name
install -Dpm0644 man1/%name.1 %buildroot%_man1dir/%name.1

%files
%doc LICENSE legalcode.txt
%doc README.md
%_bindir/%name
%_man1dir/%name.1*

%changelog
* Thu Mar 02 2023 L.A. Kostis <lakostis@altlinux.ru> 3.0.23.01.25-alt1
- NMU:
  + Updated to 3.0.23.01.25.

* Tue May 04 2021 L.A. Kostis <lakostis@altlinux.ru> 3.0.21.02.21-alt1
- NMU:
  + Updated to 3.0.21.02.21.

* Sat Jun 30 2018 Vitaly Lipatov <lav@altlinux.ru> 2.2.18.04.06-alt1
- new version 2.2.18.04.06 (with rpmrb script)

* Mon Nov 06 2017 Vitaly Lipatov <lav@altlinux.ru> 2.2.17.10.25-alt1
- new version 2.2.17.10.25 (with rpmrb script)

* Sun Aug 06 2017 Vitaly Lipatov <lav@altlinux.ru> 2.2.17.06.14-alt1
- new version 2.2.17.06.14 (with rpmrb script)

* Sat Jun 17 2017 Vitaly Lipatov <lav@altlinux.ru> 2.1.17.02.09-alt1
- initial build for ALT Sisyphus

* Sat Feb 11 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.17.02.09-1
- Update to 2.1.17.02.09

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.16.01.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 31 2016 Igor Gnatenko <ignatenko@redhat.com> - 2.1.16.01.12-2
- Rebuild for OpenCL 2.1
- Cleanups and fixes in spec

* Sun Feb 07 2016 Fabian Deutsch <fabiand@fedoraproject.org> - 2.1.16.01.12-1.0.git20160207.f951686
- Update to the latest upstream

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.8.git20150215.94fdb47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.7.git20150215.94fdb47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Feb 15 2015 Fabian Deutsch <fabiand@fedoraproject.org> - 0.1.0-0.6.git20150215.94fdb47
- Update to the latest upstream

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.5.git20140422.7050765
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.4.git20140422.7050765
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 22 2014 Fabian Deutsch <fabiand@fedoraproject.org> - 0.1-0.3.git20140422.7050765
- Fix two bugs related to platforms without devices

* Tue Oct 01 2013 Fabian Deutsch <fabiand@fedoraproject.org> - 0.1-0.2.git20131001.7f44937
- Remove unused ldconfig and opencl-filesystem

* Tue Oct 01 2013 Fabian Deutsch <fabiand@fedoraproject.org> - 0.1-0.1.git20131001.7f44937
- Initial package
