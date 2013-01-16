%define realname PyYAML

Name:           python-module-pyyaml
Version:        3.10
Release:        alt1
Summary:        YAML parser and emitter for Python

Group:          Development/Python
License:        MIT
URL:            http://pyyaml.org/
Source0:        http://pyyaml.org/download/pyyaml/%realname-%version.tar.gz

#BuildArch:      noarch
BuildRequires(pre): rpm-build-python
BuildRequires:  python-devel
BuildRequires:  python-module-distribute

BuildRequires:  libyaml-devel
Provides:       %realname = %version-%release

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-distribute

%description
YAML is a data serialization format designed for human readability and
interaction with scripting languages.  PyYAML is a YAML parser and
emitter for Python.

PyYAML features a complete YAML 1.1 parser, Unicode support, pickle
support, capable extension API, and sensible error messages.  PyYAML
supports standard YAML tags and provides Python-specific tags that
allow to represent an arbitrary Python object.

PyYAML is applicable for a broad range of tasks from complex
configuration files to object serialization and persistance.

%package -n python3-module-pyyaml
Summary: YAML parser and emitter for Python
Group: Development/Python

%description -n python3-module-pyyaml
YAML is a data serialization format designed for human readability and
interaction with scripting languages.  PyYAML is a YAML parser and
emitter for Python.

PyYAML features a complete YAML 1.1 parser, Unicode support, pickle
support, capable extension API, and sensible error messages.  PyYAML
supports standard YAML tags and provides Python-specific tags that
allow to represent an arbitrary Python object.

PyYAML is applicable for a broad range of tasks from complex
configuration files to object serialization and persistance.


%prep
%setup -q -n %realname-%version
chmod a-x examples/yaml-highlight/yaml_hl.py
mkdir build-python3
cp -a * build-python3 ||:

%build
%python_build
pushd build-python3
%python3_build
popd

%install
%python_install
pushd build-python3
%python3_install
popd


%files
%doc CHANGES LICENSE PKG-INFO README examples
%python_sitelibdir/yaml
%python_sitelibdir/*.so
%python_sitelibdir/%{realname}*.egg-info


%files -n python3-module-pyyaml
%doc CHANGES LICENSE PKG-INFO README examples
%python3_sitelibdir/yaml
%python3_sitelibdir/*.so
%python3_sitelibdir/%{realname}*.egg-info


%changelog
* Wed Jan 16 2013 Andrey Cherepanov <cas@altlinux.org> 3.10-alt1
- Initial build in Sisyphus
