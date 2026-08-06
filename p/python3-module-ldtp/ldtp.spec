%define _unpackaged_files_terminate_build 1
%define pypi_name ldtp

%def_without check

Name: python3-module-%pypi_name
Version: 3.5.0
Release: alt1
Summary: Linux Desktop Testing Project Version 2
License: LGPL-2.1
Group: Development/Python3
Url: http://ldtp.freedesktop.org/
Vcs: https://github.com/ldtp/ldtp2
BuildArch: noarch

Source: %name-%version.tar
Patch: ldtp-py3-compat.patch
Patch1: ldtp-imports-qualify.patch

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3-module-twisted-core
BuildRequires: python3-module-twisted-web
BuildRequires: python3(pyatspi)


%if_with check
BuildRequires: python3(pytest)
%endif

%py3_provides %pypi_name

%add_python3_self_prov_path %{python3_sitelibdir}/ldtp
%add_python3_self_prov_path %{python3_sitelibdir}/ldtpd
%add_python3_self_prov_path %{python3_sitelibdir}/ldtputils
%add_python3_self_prov_path %{python3_sitelibdir}/ooldtp
%add_python3_req_skip waiters

%description
Linux Desktop Testing Project Version 2

%prep
%setup -q
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README AUTHORS COPYING NEWS INSTALL Doxyfile
%doc doc/
%doc examples/
%doc Example/
%doc ldtp/Perl/README
%_bindir/ldtp
%python3_sitelibdir/%{pypi_name}/
%python3_sitelibdir/ldtpd/
%python3_sitelibdir/ldtputils/
%python3_sitelibdir/ooldtp/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Aug 06 2026 Pavel Shilov <zerospirit@altlinux.org> 3.5.0-alt1
- Initial build for Sisyphus.
