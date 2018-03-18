# BEGIN SourceDeps(oneline):
BuildRequires: swig unzip
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global debug_package %{nil}
%define libnamedev libsnark-supercop-devel-static

Name:           libsnark-supercop
Version:        20141014
Release:        alt1_3
Summary:        Subset of the supercop sources used in the libsnark
Group:		System/Libraries
License:        MIT
URL:            https://github.com/mbbarbosa/libsnark-supercop
Source0:        https://github.com/mbbarbosa/libsnark-supercop/archive/libsnark-supercop-master.zip
Source44: import.info

%description
Supercop permits automatically detecting the best compilation options for each 
of these algorithms in any given platform.

For optimal performance, Supercop should be used to determine the compilation 
options for each specific file in the target machine.


%package        -n %libnamedev
Group: System/Libraries
Summary:        Development files for %{name}

%description    -n %libnamedev
Supercop permits automatically detecting the best compilation options for each 
of these algorithms in any given platform.

For optimal performance, Supercop should be used to determine the compilation 
options for each specific file in the target machine.


%prep
%setup -q  -n libsnark-supercop-master

%build
sh do

%install
mkdir -p %{buildroot}%{_includedir}/supercop
mkdir -p %{buildroot}%{_libdir}/
install -p include/{crypto_core_aes128encrypt.h,crypto_hash_sha256.h,crypto_hash_sha512.h,crypto_sign_ed25519.h,crypto_sign.h,crypto_verify_16.h,crypto_verify_32.h,crypto_verify_8.h,randombytes.h}  %{buildroot}%{_includedir}/supercop
install -p lib/libsupercop.a  %{buildroot}%{_libdir}

%files -n %libnamedev
%doc README.md
%{_includedir}/supercop/*
%{_libdir}/libsupercop.a



%changelog
* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 20141014-alt1_3
- new version

