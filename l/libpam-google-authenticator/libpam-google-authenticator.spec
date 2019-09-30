%define 	projname google-authenticator
Name:           libpam-%{projname}
Version:        1.06
Release:        alt1
Summary:        One-time passcode support using open standards
#Summary(ru_RU.UTF8): 
License:        ASL 2.0
URL:            https://github.com/google/google-authenticator-libpam
Packager: 	Alexei Mezin <alexvm@altlinux.org>
Vendor: 	ALT Linux Team
Group:		System/Libraries


Source0:        %{name}-%{version}.tar.gz
# Automatically added by buildreq on Mon Sep 30 2019
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 perl python-base python-modules python3 python3-base python3-dev sh4
##BuildRequires: glibc-devel-static libdb4-devel libpam-devel python3-module-mpl_toolkits python3-module-yieldfrom selinux-policy

BuildRequires: libpam-devel

##BuildRequires:  gcc
##BuildRequires:  pam-devel
##BuildRequires:  libtool


%description
The Google Authenticator package contains a pluggable authentication
module (PAM) which allows login using one-time passcodes conforming to
the open standards developed by the Initiative for Open Authentication
(OATH) (which is unrelated to OAuth).

Passcode generators are available (separately) for several mobile
platforms.

These implementations support the HMAC-Based One-time Password (HOTP)
algorithm specified in RFC 4226 and the Time-based One-time Password
(TOTP) algorithm specified in RFC 6238.

%prep

%setup -q 
##-n %{projname}-libpam-%{version}

%build
%autoreconf -i
%configure --libdir=/%_lib
%make 

%install
##rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm $RPM_BUILD_ROOT/%{_lib}/security/pam_google_authenticator.la

%files
##%_libdir/security/pam_google_authenticator.so
%_pam_modules_dir/pam_google_authenticator.so
%_bindir/*
%_docdir/%{projname}/README.md
%_docdir/%{projname}/totp.html
%_docdir/%{projname}/FILEFORMAT
%_man1dir/*
%_man8dir/*


%changelog
* Mon Sep 30 2019 Alexei Mezin <alexvm@altlinux.org> 1.06-alt1
- New initial build
* Thu Mar 07 2013 Denis Baranov <baraka@altlinux.ru> 1.0-alt1
- Initial build for ALTLinux


