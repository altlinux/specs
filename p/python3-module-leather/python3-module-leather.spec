%define  modulename leather

Name:    python3-module-%modulename
Version: 0.3.4
# Added python 3.10 support in this commit
Release: alt1.ad57c77.1

Summary: Python charting for 80%% of humans.
License: MIT
Group:   Development/Python3
URL:     https://github.com/wireservice/leather

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source:  %modulename-%version.tar

%description
Leather is the Python charting library for those who need charts now and don't
care if they're perfect.

Leather isn't picky. It's rough. It gets dirty. It looks sexy just hanging on
the back of a chair. Leather doesn't need your accessories. Leather is how
Snake Plissken would make charts.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info

%changelog
* Tue Apr 25 2023 Mikhail Gordeev <obirvalger@altlinux.org> 0.3.4-alt1.ad57c77.1
- Update version to 0.3.4 and commit ad57c770490927095d5ea376ddb3cec7d7ea3c3f

* Wed Feb 07 2018 Mikhail Gordeev <obirvalger@altlinux.org> 0.3.3-alt1
- Initial build for Sisyphus
