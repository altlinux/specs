%def_with dcmtk
%define _unpackaged_files_terminate_build 1
%define soname 3
%set_autoconf_version 2.71

Name: biosig
Version: 2.6.1
Release: alt2

Summary: Reading and writing routines for different biosignal data formats
License: GPL-3.0+
Group: Sciences/Medicine

Url: https://biosig.sourceforge.net/
Source: %name-%version.tar

Patch1: %name-alt-build-2.5.2.patch
Patch2: biosig-2.6.1-alt-python-install.patch

BuildRequires(pre): rpm-build-python3 rpm-build-pyproject
BuildRequires: python3-devel libnumpy-py3-devel
BuildRequires: python3-module-setuptools python3-module-build python3-module-wheel
BuildRequires: gcc-c++
BuildRequires: libalsa-devel
BuildRequires: libb64-devel
BuildRequires: libsuitesparse-devel
BuildRequires: autoconf_2.71
%if_with dcmtk
BuildRequires: libdcmtk-devel
%endif
BuildRequires: zlib-devel
BuildRequires: tinyxml-devel

Requires: lib%name%soname = %EVR

%description
BioSig is an open source software library for biomedical signal processing,
featuring for example the analysis of biosignals such as
the electroencephalogram (EEG), electrocorticogram (ECoG),
electrocardiogram (ECG), electrooculogram (EOG), electromyogram (EMG),
respiration, and so on. Major application areas are: Neuroinformatics,
brain-computer interfaces, neurophysiology, psychology,
cardiovascular systems and sleep research. The aim of the BioSig project
is to foster research in biomedical signal processing by
providing open source software tools for many different applications.
Generally, many concerns have to be addressed in this scientific field.
BioSig handles this by providing solutions for data acquisition,
artifact processing, quality control, feature extraction, classification,
modeling, data visualization, and so on.

Everything in this project is freely available under the
GNU General Public License.

%package -n lib%name%soname
Summary: Reading and writing routines for different biosignal data formats
Group: System/Libraries

%description -n lib%name%soname
BioSig is an open source software library for biomedical signal processing,
featuring for example the analysis of biosignals such as
the electroencephalogram (EEG), electrocorticogram (ECoG),
electrocardiogram (ECG), electrooculogram (EOG), electromyogram (EMG),
respiration, and so on. Major application areas are: Neuroinformatics,
brain-computer interfaces, neurophysiology, psychology,
cardiovascular systems and sleep research. The aim of the BioSig project
is to foster research in biomedical signal processing by
providing open source software tools for many different applications.
Generally, many concerns have to be addressed in this scientific field.
BioSig handles this by providing solutions for data acquisition,
artifact processing, quality control, feature extraction, classification,
modeling, data visualization, and so on.

Everything in this project is freely available under the
GNU General Public License.

%package devel
Summary: Reading and writing routines for different biosignal data formats
Group: Development/C++
Requires: %name = %EVR
Requires: lib%name%soname = %EVR

%description devel
BioSig is an open source software library for biomedical signal processing,
featuring for example the analysis of biosignals such as
the electroencephalogram (EEG), electrocorticogram (ECoG),
electrocardiogram (ECG), electrooculogram (EOG), electromyogram (EMG),
respiration, and so on. Major application areas are: Neuroinformatics,
brain-computer interfaces, neurophysiology, psychology,
cardiovascular systems and sleep research. The aim of the BioSig project
is to foster research in biomedical signal processing by
providing open source software tools for many different applications.
Generally, many concerns have to be addressed in this scientific field.
BioSig handles this by providing solutions for data acquisition,
artifact processing, quality control, feature extraction, classification,
modeling, data visualization, and so on.

Everything in this project is freely available under the
GNU General Public License.

%package -n python3-module-%name
Summary: Reading and writing routines for different biosignal data formats
Group: Development/Python3
Requires: lib%name%soname = %EVR

%description -n python3-module-%name
BioSig is an open source software library for biomedical signal processing,
featuring for example the analysis of biosignals such as
the electroencephalogram (EEG), electrocorticogram (ECoG),
electrocardiogram (ECG), electrooculogram (EOG), electromyogram (EMG),
respiration, and so on. Major application areas are: Neuroinformatics,
brain-computer interfaces, neurophysiology, psychology,
cardiovascular systems and sleep research. The aim of the BioSig project
is to foster research in biomedical signal processing by
providing open source software tools for many different applications.
Generally, many concerns have to be addressed in this scientific field.
BioSig handles this by providing solutions for data acquisition,
artifact processing, quality control, feature extraction, classification,
modeling, data visualization, and so on.

Everything in this project is freely available under the
GNU General Public License.


%prep
%setup
%patch1 -p1
%patch2 -p1

# sigviewer isn't built here. don't install it's manpage either
rm -f biosig4c++/doc/sigviewer.1

# same
rm -f biosig4c++/doc/mexSLOAD.1

rm -f biosig4c++/python/{demo2,example}.py

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/*
%_man1dir/*.1*

%files -n lib%name%soname
%doc COPYING
%doc README CITATION
%_libdir/*.so.%{soname}

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_datadir/%name

%files -n python3-module-%name
%python3_sitelibdir/%{name}*.so
%python3_sitelibdir/*-info/METADATA

%changelog
* Wed Aug 07 2024 Anton Farygin <rider@altlinux.ru> 2.6.1-alt2
- set the version of autoconf to 2.71 to simplify the build
  into the old branches

* Mon Aug 05 2024 Anton Farygin <rider@altlinux.ru> 2.6.1-alt1
- 2.6.0 -> 2.6.1

* Wed Apr 03 2024 Anton Farygin <rider@altlinux.ru> 2.6.0-alt1
- 2.5.2 -> 2.6.0
- added upstream fix against numpy.distutils deprecation

* Fri Jan 19 2024 Alexey Shemyakin <alexeys@altlinux.org> 2.5.2-alt1
- Update to version 2.5.2.

* Tue Dec 19 2023 Grigory Ustinov <grenka@altlinux.org> 2.3.1-alt2.1
- NMU: Add build dependency on setuptools.

* Wed Jan 19 2022 Michael Shigorin <mike@altlinux.org> 2.3.1-alt2
- Introduce dcmtk knob (on by default).

* Mon Jul 26 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.3.1-alt1
- Initial build for ALT.

