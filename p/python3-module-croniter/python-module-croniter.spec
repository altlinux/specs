%global oname croniter

Name: python3-module-%oname
Version: 1.0.11
Release: alt1

Summary: Iteration for datetime object with cron like format
License: MIT
Group: Development/Python3
Url: http://github.com/kiorky/croniter

BuildArch: noarch

Source0: %oname-%version.tar

BuildRequires: rpm-build-python3 python3(setuptools) python3(dateutil)
# tests
BuildRequires: python3(pytz)
BuildRequires: python3(pytest)

%description
Croniter provides iteration for datetime object with cron like format.

%prep
%setup -q -n %oname-%version

# Remove bundled egg-info
rm -rf %oname.egg-info
# Remove reundant script header to avoid rpmlint warnings
find -name \*.py -exec sed -i '/\/usr\/bin\/env python/{d;q}' {} +

%build
%python3_build

%install
%python3_install

%check
# TimezoneDateutil test fails, see https://bugzilla.altlinux.org/show_bug.cgi?id=39164
py.test3 -v ||:

%files
%doc README.rst docs/LICENSE
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py?.?.egg-info

%changelog
* Mon Apr 12 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.11-alt1
- 1.0.11

* Fri Jul 17 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.34-alt1
- 0.3.34 released

* Tue Apr 14 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.3.4-alt3
- Build for python2 removal.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.3.4-alt1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.4-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Aug 11 2014 Lenar Shakirov <snejok@altlinux.ru> 0.3.4-alt1
- First build for ALT (based on Fedora 0.3.4-4.fc21.src)

