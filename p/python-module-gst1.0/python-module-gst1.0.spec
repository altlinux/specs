%define _name gst-python
%define ver_major 1.4
%define gst_api_ver 1.0
%define _gst_libdir %_libdir/gstreamer-%gst_api_ver

Name: python-module-gst%gst_api_ver
Version: %ver_major.0
Release: alt1.1

Summary: Python bindings for GStreamer-1.0
Group: Development/Python
License: LGPL2.1+
Url: http://gstreamer.freedesktop.org/

Source: http://gstreamer.freedesktop.org/src/%_name/%_name-%version.tar.xz
#Source: %_name-%version.tar

BuildRequires: rpm-build-gir
BuildRequires: gst-plugins%gst_api_ver-devel >= %ver_major
BuildRequires: python-module-pygobject3-devel python-modules-compiler
# for python3
BuildRequires: rpm-build-python3 python3-devel python3-module-pygobject3-devel

%description
This module contains a wrapper that allows GStreamer applications
to be written in Python.

%package -n python3-module-gst%gst_api_ver
Summary: Python3 bindings for GStreamer-1.0
Group: Development/Python3
License: LGPL2.1+

%description -n python3-module-gst%gst_api_ver
This module contains a wrapper that allows GStreamer applications
to be written in Python3.

%prep
%setup -n %_name-%version -a0
mv %_name-%version py3build
# skip usless check for Windows
subst '/^AM_CHECK_PYTHON_LIBS/d' configure.ac py3build/configure.ac
# make plugin parallel installable
subst 's/libgstpythonplugin/libgstpython3plugin/' py3build/plugin/Makefile.am

%build
%autoreconf
%configure
%make_build

pushd py3build
export PYTHON=python3
%autoreconf
%configure
%make_build
popd

%install
%makeinstall_std

pushd py3build
%makeinstall_std
popd

%files
%_gst_libdir/libgstpythonplugin.so
%python_sitelibdir/gi/overrides/*
%doc AUTHORS NEWS

%exclude %python_sitelibdir/gi/overrides/*.la

%files -n python3-module-gst%gst_api_ver
%_gst_libdir/libgstpython3plugin.so
%python3_sitelibdir/gi/overrides/*

%exclude %python3_sitelibdir/gi/overrides/*.la
%exclude %_gst_libdir/*.la

%changelog
* Tue Nov 04 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1.1
- fixed name of python3 package

* Mon Nov 03 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- first build for Sisyphus

