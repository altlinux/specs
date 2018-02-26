Version: 0.5.0
Release: alt1.1
%setup_python_module pythonwifi
Name: %packagename

Summary: Python binding for the wireless (wifi) extensions
License: GPL
Group: Development/Python
Packager: Python Development Team <python at packages.altlinux.org>

Url: http://pythonwifi.wikispot.org/
Source: http://download.berlios.de/pythonwifi/python-wifi-0.5.0.tar.bz2
BuildArch: noarch

# Automatically added by buildreq on Sat Dec 16 2006 (-bi)
BuildRequires: python-devel python-modules-encodings

%description
This module facilitates read only access to wireless (wifi) cards.

This module is built for python %_python_version

%package -n %name-doc
Summary: %modulename documentation and example programs
Group: Development/Python
Prefix: %prefix
Requires: %name = %version

%description -n  %name-doc
%modulename facilitates read only access to wireless (wifi) cards.
Install this package if you need API documentation
and examples for this module

%prep
%setup -n python-wifi

# borrowed from dag's spec too
cat <<'EOF' >setup.py
import os, string, sys
from distutils.core import setup

def main():
	setup(
		name="%name",
		version="%version",
		description="%summary",
		author="Dag Wieers",
		author_email="dag@wieers.com, http://dag.wieers.com/, dag.wieers@gmail.com",
		maintainer="Dag Wieers",
		maintainer_email="dag@wieers.com",
		url="%url",
		license="%license",
		platforms="UNIX",
		long_description="""%description""",
		keywords=["wireless extensions", "wifi", "iwlibs"],
		packages=['pythonwifi'],
		package_dir={'pythonwifi': 'pythonwifi'},
#		py_modules=["pythonwifi"],
	)

if __name__ == "__main__": main()
EOF

### Fix permissions on examples and tests
chmod a+x examples/*.py tests/*.py

%build
mkdir -p buildroot

# Unfortunately build and install steps should be done at once
# because otherwise .pyo files won't get into INSTALLED_FILES
# record	--> borrowed from python policy's spec sample

CFLAGS="%optflags" python setup.py \
	install --optimize=1 \
		--root=`pwd`/buildroot \
		--record=INSTALLED_FILES

%install
cp -pr buildroot %buildroot
unset RPM_PYTHON

%files -f INSTALLED_FILES
%doc README

%files -n %name-doc
%doc docs/ examples/ tests/

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.0-alt1.1
- Rebuild with Python-2.7

* Tue Aug 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1
- Version 0.5.0

* Mon Nov 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt3
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.3-alt2.1
- Rebuilt with python-2.5.

* Wed Mar 21 2007 Michael Shigorin <mike@altlinux.org> 0.3-alt2
- fixed doc subpackage requirements

* Sat Dec 16 2006 Michael Shigorin <mike@altlinux.org> 0.3-alt1
- built for ALT Linux (recent dstat dependency)
- based on this spec: Dag Wieers <dag/wieers.com> - 0.3-2 - 4635/dag
  + spec *cleanup*
  + buildreq
  + NB: buildroot population is hackery this way :-(
