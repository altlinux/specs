%def_enable snapshot
%def_without python3
%def_enable check

Name: volume_key
Version: 0.3.12
Release: alt2

Summary: An utility for manipulating storage encryption keys and passphrases
License: GPLv2
Group: System/Configuration/Hardware
Url: https://pagure.io/volume_key

%if_disabled snapshot
Source: https://fedorahosted.org/releases/v/o/%name/%name-%version.tar.xz
%else
Vcs: https://pagure.io/volume_key.git
Source: %name-%version.tar
%endif

%define gpg_ver 2.2.7
%define gpgme_ver 1.11.0

Requires: lib%name = %version-%release
Requires: pinentry-gtk

BuildRequires: glib2-devel libcryptsetup-devel gnupg2 >= %gpg_ver
BuildRequires: libgpgme-devel >= %gpgme_ver libblkid-devel libnss-devel
%{?_with_python3:BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel swig}
%{?_enable_check:BuildRequires: %_bindir/certutil}

%description
This package provides a command-line tool for manipulating storage volume
encryption keys and storing them separately from volumes.

The main goal of the software is to allow restoring access to an encrypted
hard drive if the primary user forgets the passphrase.  The encryption key
back up can also be useful for extracting data after a hardware or software
failure that corrupts the header of the encrypted volume, or to access the
company data after an employee leaves abruptly.

%package -n lib%name
Summary: A library for manipulating storage encryption keys and passphrases
Group: System/Libraries
Requires: gnupg2 >= %gpg_ver

%description -n lib%name
This package provides libvolume_key, a library for manipulating storage volume
encryption keys and storing them separately from volumes.

The main goal of the software is to allow restoring access to an encrypted
hard drive if the primary user forgets the passphrase.  The encryption key
back up can also be useful for extracting data after a hardware or software
failure that corrupts the header of the encrypted volume, or to access the
company data after an employee leaves abruptly.

%package -n lib%name-devel
Summary: A library for manipulating storage encryption keys and passphrases
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package provides libvolume_key, a library for manipulating storage volume
encryption keys and storing them separately from volumes.

The main goal of the software is to allow restoring access to an encrypted
hard drive if the primary user forgets the passphrase.  The encryption key
back up can also be useful for extracting data after a hardware or software
failure that corrupts the header of the encrypted volume, or to access the
company data after an employee leaves abruptly.

%package -n python3-module-%name
Summary: Python3 bindings for libvolume_key
Group: Development/Python3
Requires: lib%name = %version-%release

%description -n python3-module-%name
This package provides Python3 bindings for libvolume_key, a library for
manipulating storage volume encryption keys and storing them separately from
volumes.

The main goal of the software is to allow restoring access to an encrypted
hard drive if the primary user forgets the passphrase.  The encryption key
back up can also be useful for extracting data after a hardware or software
failure that corrupts the header of the encrypted volume, or to access the
company data after an employee leaves abruptly.

volume_key currently supports only the LUKS volume encryption format.  Support
for other formats is possible, some formats are planned for future releases.

%prep
%setup

%build
%autoreconf
%configure --without-python %{subst_with python3}
%make_build

%install
%makeinstall_std
%find_lang %name

%check
%make check

%files
%_bindir/%name
%_man8dir/%name.8.*
%doc README contrib

%files -n lib%name -f %name.lang
%_libdir/lib%name.so.*
%doc AUTHORS ChangeLog NEWS

%files -n lib%name-devel
%_includedir/%name/
%_libdir/lib%name.so

%if_with python3
%files -n python3-module-%name
%python3_sitelibdir/_%name.so
%python3_sitelibdir/%name.py*
%python3_sitelibdir/__pycache__/%{name}*
%exclude %python3_sitelibdir/_%name.la
%endif

%changelog
* Thu Dec 03 2020 Yuri N. Sedunov <aris@altlinux.org> 0.3.12-alt2
- updated to 0.3.12-5-g28e542c (Add support for higher versions of LUKS)
- disabled useless python3 module

* Fri Feb 22 2019 Yuri N. Sedunov <aris@altlinux.org> 0.3.12-alt1
- updated to 0.3.12-2-ge236747

* Wed Jul 18 2018 Yuri N. Sedunov <aris@altlinux.org> 0.3.11-alt1
- 0.3.11 (switched to python3)
- %%check section

* Mon May 21 2018 Yuri N. Sedunov <aris@altlinux.org> 0.3.10-alt1
- 0.3.10

* Mon Jan 29 2018 Yuri N. Sedunov <aris@altlinux.org> 0.3.9-alt2
- rebuilt against libcryptsetup.so.12

* Tue Oct 18 2016 Yuri N. Sedunov <aris@altlinux.org> 0.3.9-alt1
- 0.3.9 (0.3.9-8-gd4b00ce)

