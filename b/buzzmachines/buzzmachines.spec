%define origname buzzmachines

Name: %origname
Version: 20100517
Release: alt1.git20140910
Summary: This module provide a set of opensource buzzmachines

License: %gpl2plus
Group: Sound
Url: http://www.buzztard.org
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Buzztrax/buzzmachines.git
Source: %origname-%version.tar

Requires: libbml
BuildRequires(pre): rpm-build-licenses rpm-build-buzztard
BuildPreReq: gcc-c++
BuildPreReq: libbml-devel

%description
This module provide a set of buzzmachines that have been released as open source.
They can be used via bml library or in all gstreamer app via bml+gstbml.

%prep
%setup -n %origname-%version

%build
%ifarch %ix86
BML_PATH=%buzz_gear_dir:%buzz_gear_dir/Effects:%buzz_gear_dir/Generators
%else
BML_PATH=%buzz_gear_dir
%endif
export BML_PATH
./autogen.sh \
	--noconfigure \
	--debug \
	--prefix=%prefix
%configure \
	--enable-dependency-tracking \
	--enable-shared \
	--with-gnu-ld \
	--enable-debug \
	--%buzz_enable_static-static
%make_build

%install
%makeinstall_std

%files
%buzz_gear_dir/*.so
%_datadir/Gear
%_datadir/buzztrax

%changelog
* Sun Sep 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20100517-alt1.git20140910
- Version 20100517

* Sat Feb 07 2009 Eugeny A. Rostovtsev (REAL) <real@altlinux.org> 0.4.0-alt2.svn20081222
- rebuild for reformed libbml

* Tue Jan 06 2009 Eugeny A. Rostovtsev (REAL) <real@altlinux.org> 0.4.0-alt1.svn20081222
- Revise BuildRequires
- Add svn date into release
- Remove autogen.sh call
- Remove --prefix parameter

* Fri Jan 02 2009 Eugeny A. Rostovtsev (REAL) <real@altlinux.org> 0.4.0-alt1
- Initial build for Sisyphus

