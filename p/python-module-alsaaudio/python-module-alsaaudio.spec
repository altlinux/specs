%define oname pyalsaaudio
%def_with python3

Name: python-module-alsaaudio
Version: 0.7
Release: alt1

Summary: Wrapper for accessing the ALSA API from Python

License: PSF
Group: Development/Python
Url: http://pyalsaaudio.sourceforge.net/

%setup_python_module %oname
%define _python_egg_info %python_sitelibdir/%oname-%version-py%_python_version.egg-info

Source: http://prdownloads.sf.net/%oname/%oname-%version.tar.bz2

# Automatically added by buildreq on Fri Jan 09 2009
BuildRequires: libalsa-devel python-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
%endif

%description
This package contains wrappers for accessing the ALSA API from Python. It
is currently fairly complete for PCM devices and Mixer access. MIDI
sequencer support is low on our priority list, but volunteers are welcome.

%if_with python3
%package -n python3-module-alsaaudio
Summary: Wrapper for accessing the ALSA API from Python 3
Group: Development/Python3

%description -n python3-module-alsaaudio
This package contains wrappers for accessing the ALSA API from Python 3. It
is currently fairly complete for PCM devices and Mixer access. MIDI
sequencer support is low on our priority list, but volunteers are welcome.
%endif

%prep
%setup -q -n %oname-%version
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc README TODO
%python_sitelibdir/alsaaudio.so
%_python_egg_info

%if_with python3
%files -n python3-module-alsaaudio
%python3_sitelibdir/*
%endif

%changelog
* Mon Apr 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1
- Verson 0.7 (ALT #27183)
- Added module for Python 3

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4-alt1.1.1
- Rebuild with Python-2.7

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.1
- Rebuilt with python 2.6

* Fri Jan 09 2009 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt1
- write spec from scratch, new version

* Mon Jan 28 2008 Grigory Batalov <bga@altlinux.ru> 0.1-alt2.1.1
- Rebuilt with python-2.5.

* Mon Jan 28 2008 Grigory Batalov <bga@altlinux.ru> 0.1-alt2.1
- Remove python version from the package name.

* Tue Mar 29 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.1-alt1.1
- Rebuilt with python-2.4.

* Sun Dec 05 2004 Ivan Fedorov <ns@altlinux.ru> 0.1-alt1
- Initial build for ALT Linux
