%define _unpackaged_files_terminate_build 1

%def_with check

%define wmm_dir geomag/model_data/

Name: python3-module-geomag
Version: 0.9.2015
Release: alt1.1

Summary: Calculates magnetic variation/declination
License: LGPL-2.0-or-later
Group: Sciences/Geosciences
URL: https://github.com/rinigus/geomag
VCS: https://github.com/rinigus/geomag.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%prep
%setup

%description
Calculates magnetic variation/declination for any
latitude/longitude/altitude, for any date. Uses the NOAA
National Geophysical Data Center.

%build
%pyproject_build

%install
%pyproject_install

install -pD -m644 -t %buildroot/%python3_sitelibdir/%wmm_dir/ \
    %wmm_dir/WMM.COF \
    %wmm_dir/WMM2015.COF
rm -f %python3_sitelibdir/%wmm_dir/WMM2015.COF

%check
sed -i 's/WMM\.COF/WMM2015.COF/' geomag/world_magnetic_model.py
%pyproject_run_pytest -vra

%files
%python3_sitelibdir/geomag/
%python3_sitelibdir/geomag-%version.dist-info/

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 0.9.2015-alt1.1
- Demodernized packaging.

* Thu Oct 16 2025 Egor Shestakov <ved@altlinux.org> 0.9.2015-alt1
- Initial build.
