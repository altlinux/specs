Name:		ext4magic
Version:	0.3.2
Release:	alt1
Summary:	Can help to recover deleted files on ext3/4 filesystems
License:	GPLv2+
Group:		System/Kernel and hardware
Url:		http://sourceforge.net/projects/ext4magic/
Source0:	http://sourceforge.net/projects/ext4magic/files/ext4magic-0.3.2.tar.gz

Patch0:		%name-0.3.2_alt_libmagic_test_off.patch

# Automatically added by buildreq on Wed Aug 16 2017 (-bi)
# optimized out: elfutils gnu-config libcom_err-devel perl python-base python-modules python3 python3-base rpm-build-python3 xz
BuildRequires: bzlib-devel libblkid-devel libe2fs-devel libmagic-devel libuuid-devel zlib-devel

%description
ext4magic is a small tool for Linux administration, it can help to recover
accidentally deleted or overwritten files from an ext3 or ext4 file systems.
Especially private computers often lack an adequate and reliable backup or the
backup interval is too large lack of capacity. After some minor or major
accidents console or script often arises the question, how can I just restore
the deleted files back?

%prep
%setup
%patch0 -p1

%build
%configure \
	--enable-file-attr \
	--enable-expert-mode
%make_build

%install
%makeinstall

%files
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%_sbindir/*
%_man8dir/*

%changelog
* Wed Aug 16 2017 Motsyo Gennadi <drool@altlinux.ru> 0.3.2-alt1
- initial build for ALT Linux
