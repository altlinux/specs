%define srcname ezdxf

#def_disable check

Name: python3-module-ezdxf
Version: 0.16.3
Release: alt1
Summary: Python 3 package for manipulating DXF drawings
License: MIT
Group: Development/Python3
URL: https://ezdxf.mozman.at/
# Source-url: https://github.com/mozman/ezdxf/archive/v%version.tar.gz
Source: %srcname-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-Cython
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_disabled check
%else
BuildRequires: python3-module-pytest
#BuildRequires: python3-module-geomdl
%endif

%description
A Python package to create and modify DXF drawings, independent from the
DXF version.

%prep
%setup -n %srcname-%version
# remove unused script interpreter line
sed -i '1 {/env python/ d}' src/ezdxf/addons/drawing/qtviewer.py

%build
%python3_build

%install
%python3_install

%check
export PYTHONPATH=%buildroot/%python3_sitelibdir/
# text2path: some tests only work with the presence of Arial font family
py.test3 -k "not test_814_text2path \
	and not TestNurbsPythonCorrectness \
	and not test_rational_spline_curve_points_by_nurbs_python \
	and not test_rational_spline_derivatives_by_nurbs_python \
	and not test_from_nurbs_python_curve_to_ezdxf_bspline \
	and not test_from_ezdxf_bspline_to_nurbs_python_curve_non_rational \
	and not test_from_ezdxf_bspline_to_nurbs_python_curve_rational"

%files
%doc README.md
%_bindir/ezdxf
%python3_sitelibdir/ezdxf-%{version}*info
%python3_sitelibdir/ezdxf

%changelog
* Fri Jul 30 2021 Anton Midyukov <antohami@altlinux.org> 0.16.3-alt1
- Initial build
