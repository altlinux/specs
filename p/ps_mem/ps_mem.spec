Name: ps_mem
Version: 3.6
Release: alt1

Summary: Memory profiling tool
License: LGPLv2
Group: Monitoring

Url: https://github.com/pixelb/ps_mem
Source: https://raw.githubusercontent.com/pixelb/ps_mem/c80287d/ps_mem.py
Source1: http://www.gnu.org/licenses/lgpl-2.1.txt
Source2: https://raw.githubusercontent.com/pixelb/ps_mem/c80287d/ps_mem.1
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch
BuildRequires: python3-devel

%description
The ps_mem tool reports how much core memory is used per program
(not per process).

In detail it reports: sum(private RAM for program processes)
+ sum(Shared RAM for program processes)

The shared RAM is problematic to calculate, and the tool automatically
selects the most accurate method available for the running kernel.

%prep
%setup -T -c %name-%version
cp -a %SOURCE0 %name
cp -a %SOURCE1 LICENSE
cp -a %SOURCE2 %name.1

# use python3
#subst "s|%_bindir/env python|%__python3|" %name
#touch -r %SOURCE0 %name

%install
install -Dpm755 %name   %buildroot%_bindir/%name
install -Dpm644 %name.1 %buildroot%_man1dir/%name.1

%files
%doc LICENSE
%_bindir/%name
%_man1dir/%name.1*

%changelog
* Sat Dec 03 2016 Michael Shigorin <mike@altlinux.org> 3.6-alt1
- initial build for ALT Linux Sisyphus (based on fedora package)

* Mon Jul 11 2016 Lumir Balhar <lbalhar@redhat.com> - 3.6-2
- Fixed missing BuildRequire

* Wed Jun 08 2016 Lumir Balhar <lbalhar@redhat.com> - 3.6-1
- Latest upstream release
- Package ported to Python3 with dependencies

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 16 2015 Pádraig Brady <pbrady@redhat.com> - 3.5-1
- Latest upstream
- Depend on default python implementation

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug 14 2013 Jaromir Capik <jcapik@redhat.com> - 3.1-4
- RH man page scan (#989490)

* Thu Jul 25 2013 Jaromir Capik <jcapik@redhat.com> - 3.1-3
- Patching shebang to force python3 (#987036)

* Thu May 30 2013 Jaromir Capik <jcapik@redhat.com> - 3.1-2
- Preserving file timestamps

* Wed May 29 2013 Jaromir Capik <jcapik@redhat.com> - 3.1-1
- Initial package
