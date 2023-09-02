%define pypi_name gphoto2

Name: python3-module-%pypi_name
Version: 2.5.0
Release: alt1

Summary: Python bindings to GPhoto libraries
Group: Development/Python3
License: GPL-3.0
Url: https://pypi.python.org/pypi/%pypi_name

Source: https://pypi.io/packages/source/g/%pypi_name/%pypi_name-%version.tar.gz

%define gphoto_ver 2.5.10
BuildRequires: libgphoto2-devel >= %gphoto_ver swig
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3(wheel) python3(setuptools)

%description
python-gphoto2 is a comprehensive Python3 interface (or binding) to
libgphoto2_. It is built using SWIG_ to automatically generate the
interface code. This gives direct access to nearly all the libgphoto2_
functions, but sometimes in a rather un-Pythonic manner.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%doc README.rst


%changelog
* Sat Sep 02 2023 Yuri N. Sedunov <aris@altlinux.org> 2.5.0-alt1
- 2.5.0

* Fri Aug 25 2023 Yuri N. Sedunov <aris@altlinux.org> 2.4.0-alt1
- 2.4.0

* Tue Jul 18 2023 Yuri N. Sedunov <aris@altlinux.org> 2.3.6-alt1
- 2.3.6

* Sat Jul 08 2023 Yuri N. Sedunov <aris@altlinux.org> 2.3.5-alt1
- 2.3.5

* Wed Jul 06 2022 Yuri N. Sedunov <aris@altlinux.org> 2.3.4-alt1
- 2.3.4

* Sat Mar 05 2022 Yuri N. Sedunov <aris@altlinux.org> 2.3.3-alt1
- 2.3.3

* Fri Jan 21 2022 Yuri N. Sedunov <aris@altlinux.org> 2.3.2-alt1
- 2.3.2

* Wed Jan 05 2022 Yuri N. Sedunov <aris@altlinux.org> 2.3.1-alt1
- 2.3.1

* Tue Nov 10 2020 Yuri N. Sedunov <aris@altlinux.org> 2.2.4-alt1
- 2.2.4

* Thu Oct 29 2020 Yuri N. Sedunov <aris@altlinux.org> 2.2.3-alt1
- 2.2.3

* Thu Apr 09 2020 Yuri N. Sedunov <aris@altlinux.org> 2.2.2-alt1
- 2.2.2 (python3 only)

* Mon Mar 16 2020 Yuri N. Sedunov <aris@altlinux.org> 2.2.1-alt1
- 2.2.1

* Thu Feb 13 2020 Yuri N. Sedunov <aris@altlinux.org> 2.1.0-alt1
- 2.1.0
- disabled python2 build

* Wed Apr 24 2019 Yuri N. Sedunov <aris@altlinux.org> 2.0.0-alt1
- 2.0.0

* Wed Dec 26 2018 Yuri N. Sedunov <aris@altlinux.org> 1.9.0-alt1
- 1.9.0

* Sun Nov 25 2018 Yuri N. Sedunov <aris@altlinux.org> 1.8.5-alt1
- 1.8.5

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.8.2-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Tue Jan 16 2018 Yuri N. Sedunov <aris@altlinux.org> 1.8.2-alt1
- 1.8.2

* Thu Nov 30 2017 Yuri N. Sedunov <aris@altlinux.org> 1.8.1-alt1
- 1.8.1

* Wed Nov 01 2017 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt1
- 1.8.0

* Fri Sep 15 2017 Yuri N. Sedunov <aris@altlinux.org> 1.7.1-alt1
- 1.7.1

* Thu Jul 06 2017 Yuri N. Sedunov <aris@altlinux.org> 1.7.0-alt1
- first build for Sisyphus


