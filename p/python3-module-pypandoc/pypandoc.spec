%define pypi_name pypandoc

# online tests included
%def_disable check

Name: python3-module-%pypi_name
Version: 1.17
Release: alt1

Summary: Thin wrapper for pandoc
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/pypandoc/
BuildArch: noarch

Vcs: https://github.com/JessicaTegner/pypandoc.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3 python3(wheel) python3(hatchling)
BuildRequires: pandoc
%{?_enable_check:BuildRequires: python3(pandocfilters) /usr/bin/pdflatex}

%py3_provides %pypi_name
Requires: pandoc

%description
Thin wrapper for "pandoc" (MIT).

%prep
%setup
%python3_fix_shebang ./

%build
%pyproject_build

%install
%pyproject_install

%check
# haskell/pandoc bug
# HandshakeFailed (Error_Protocol "certificate has unknown CA" UnknownCa)
# https://bugzilla.altlinux.org/56775
export SYSTEM_CERTIFICATE_PATH=/usr/share/ca-certificates
%pyproject_run_pytest

%files
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%doc README.md


%changelog
* Tue Apr 07 2026 Yuri N. Sedunov <aris@altlinux.org> 1.17-alt1
- 1.17

* Tue Dec 16 2025 Yuri N. Sedunov <aris@altlinux.org> 1.16.2-alt1
- 1.16.2

* Wed Nov 12 2025 Yuri N. Sedunov <aris@altlinux.org> 1.16.1-alt1
- 1.16.1

* Sat Nov 08 2025 Yuri N. Sedunov <aris@altlinux.org> 1.16-alt1
- 1.16

* Mon Oct 20 2025 Yuri N. Sedunov <aris@altlinux.org> 1.15-alt1
- 1.15 (ALT #56289)

* Mon Jun 29 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.5-alt1
- Version updated to 1.5.

* Fri Dec 13 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.9.3-alt4
- build for python3 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.9.3-alt3.git20150226.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Mar 31 2016 Denis Medvedev <nbr@altlinux.org> 0.9.3-alt3.git20150226
- Recompile for changed site-packages for python3.5

* Wed Feb 24 2016 Denis Medvedev <nbr@altlinux.org> 0.9.3-alt2.git20150226
- back to sisyphus

* Fri Feb 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.3-alt1.git20150226
- Version 0.9.3

* Wed Feb 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt1.git20150204
- Version 0.9.1

* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.2-alt1.git20140529
- Initial build for Sisyphus

