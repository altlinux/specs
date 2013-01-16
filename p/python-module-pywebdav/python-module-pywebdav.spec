%define srcname PyWebDAV

Name:           python-module-pywebdav
Version:        0.9.8
Release:        alt1
Summary:        WebDAV library

Group:          Development/Python
License:        LGPLv2+
URL:            http://www.webdav.de/
Source0:        http://pywebdav.googlecode.com/files/%srcname-%version.tar.gz

BuildArch:      noarch
BuildRequires(pre): rpm-build-python
BuildRequires:  python-devel
BuildRequires:  python-module-distribute

Provides:       pywebdav = %version-%release

%description
WebDAV library for Python. WebDAV is an extension to the normal HTTP/1.1
protocol allowing the user to upload data, create collections of objects,
store properties for objects, etc.


%prep
%setup -q -n %srcname-%version
rm -f doc/INSTALL

%build
%python_build

%install
%python_install
rm -f %buildroot%_bindir/*
rm -rf %buildroot%python_sitelibdir/pywebdav/server

%files
%doc doc/*
%python_sitelibdir/pywebdav
%python_sitelibdir/%{srcname}*.egg-info


%changelog
* Wed Jan 16 2013 Andrey Cherepanov <cas@altlinux.org> 0.9.8-alt1
- Initial build in Sisyphus

