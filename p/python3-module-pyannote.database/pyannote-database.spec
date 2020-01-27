%define mname pyannote
%define oname %mname.database

Name: python3-module-%oname
Version: 2.4.3
Release: alt1

Summary: Common interface to multimedia databases.
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pyannote.database/

# https://github.com/pyannote/pyannote-database.git
Source: %name-%version.tar
Patch0: fix-detect-version.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-yaml python3-module-pandas
BuildRequires: python3-module-pyannote.core
BuildRequires: python3-module-sphinx

%py3_provides %oname


%description
%summary

%prep
%setup
%patch0 -p1

touch 'version.py'
echo '%version' >> version.py

%build
%python3_build_debug

%install
%python3_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
%if 0
%__python3 setup.py test
%endif

%files
%doc LICENSE *.md
%python3_sitelibdir/%mname/*
%python3_sitelibdir/*.egg-info


%changelog
* Mon Jan 27 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.4.3-alt1
- Initial build.

