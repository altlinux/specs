Name: nefextract 
Version: 20050816
Release: alt2

Summary: Extract full thumbnail from Nikon NEF files and auto rotate (using jpegtran)
License: GPL
Group: Graphics 
Url: http://web.mit.edu/~xsdg/Public/software/nef+workflow/nefextract.c
Packager: Anton V. Boyarshinov <boyarsh@altlinux.ru>

Requires: libjpeg-utils

Source0: nefextract.tar.gz


%description
Extract full thumbnail from Nikon NEF files and auto rotate (using jpegtran)


%prep
%setup -c


%build
%make_build

mkdir -p $RPM_BUILD_ROOT%_bindir/
install -pD nefextract $RPM_BUILD_ROOT%_bindir/

%files
%_bindir/%name

%changelog
* Thu Jan 25 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20050816-alt2
- Fixed file mode 

* Thu Jan 18 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20050816-alt1
- First build for Sisyphus 

