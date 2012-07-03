Name: python-module-python-mpd
Version: 0.2.1
Release: alt2.1.1

Summary: MPD python client library
License: GPL3
Group: Development/Python
Url: http://pypi.python.org/pypi/python-mpd/
BuildArch: noarch

Packager: Alexey Morsov <swi@altlinux.ru>
Source: %name-%version.tar

Buildrequires: python-dev >= 2.4

Requires: python >= 2.4 

%description
TagPy is a set of Python bindings for Scott Wheeler's TagLib.
It builds upon Boost.Python, a wrapper generation library which is part
of the Boost set of C++ libraries.

Just like TagLib, TagPy can:

  * read and write ID3 tags of version 1 and 2, with many supported
    frame
    types for version 2 (in MPEG Layer 2 and MPEG Layer 3, FLAC and
    MPC),
  * access Xiph Comments in Ogg Vorbis Files and Ogg Flac Files,
  * access APE tags in Musepack and MP3 files.

%prep
%setup -q

%build

%install
python setup.py install --root=$RPM_BUILD_ROOT --optimize=2 --record=INSTALLED_FILES


%files -f INSTALLED_FILES
%defattr(-,root,root)


%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.1-alt2.1.1
- Rebuild with Python-2.7

* Sat Oct 16 2010 Alexey Morsov <swi@altlinux.ru> 0.2.1-alt2.1
- inherite from gear

* Thu Oct 14 2010 Alexey Morsov <swi@altlinux.ru> 0.2.1-alt2
- fix requires (Closes: 23886)

* Wed Apr 08 2009 Alexey Morsov <swi@altlinux.ru> 0.2.1-alt1
- new version

* Thu May 01 2008 Alexey Morsov <swi@altlinux.ru> 0.2.0-alt1
- initial build for Sisyphus


