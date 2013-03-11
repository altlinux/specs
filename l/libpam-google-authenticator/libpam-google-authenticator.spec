Name: libpam-google-authenticator
Version: 1.0
Release: alt1

Summary: The PAM module can add a two-factor authentication step to any PAM-enabled application.

Url: http://code.google.com/p/google-authenticator/
License: GPL
Group: System/Libraries

Packager: Denis Baranov <baraka@altlinux.ru>

Source: http://google-authenticator.googlecode.com/files/%name-%version-source.tar

Requires: pam

# Automatically added by buildreq on Thu Mar 07 2013 (-bi)
# optimized out: elfutils python-base
BuildRequires: libpam-devel

%description
The PAM module can add a two-factor authentication step to any PAM-enabled application. It supports:
Per-user secret and status file stored in user's home directory 
Support for 30-second TOTP codes 
Support for emergency scratch codes 
Protection against replay attacks 
Key provisioning via display of QR code 
Manual key entry of RFC 3548 base32 key strings

%prep
%setup -n %name-%version

%build
%make_build

%install
install -D pam_google_authenticator.so %buildroot/%_pam_modules_dir/pam_google_authenticator.so
install -D google-authenticator %buildroot/%_bindir/google-authenticator

%files
%doc README FILEFORMAT
%_pam_modules_dir/pam_google_authenticator.so
%_bindir/google-authenticator

%changelog
* Thu Mar 07 2013 Denis Baranov <baraka@altlinux.ru> 1.0-alt1
- Initial build for ALTLinux


