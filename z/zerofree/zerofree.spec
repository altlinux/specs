Name: zerofree
Version: 1.0.2
Release: alt1

Summary: Utility to force unused ext2 inodes and blocks to zero
License: GPLv2
Group: File tools

Url: http://intgat.tigress.co.uk/rmy/uml/
Source: http://intgat.tigress.co.uk/rmy/uml/%name-%version.tgz
Source1: http://intgat.tigress.co.uk/rmy/uml/sparsify.c
Source2: http://intgat.tigress.co.uk/rmy/uml/index.html
Source3: zerofree.sgml
Patch: zerofree-1.0.2-alt-asneeded.patch
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: libe2fs-devel
BuildRequires: docbook-to-man OpenSP docbook-dtds

%description
zerofree is a utility to set unused filesystem inodes and blocks of an
ext2 filesystem to zero.  This can improve the compressibility and
privacy of an ext2 filesystem.

This tool was inspired by the ext2fs privacy (i.e. secure deletion)
patch described in a Linux kernel mailing list thread.

This package also includes the sparsify utility which will scan all
files in an ext2 filesystem and ensure that they are maximally sparse.

See http://intgat.tigress.co.uk/rmy/uml/index.html for more info.

WARNING: The filesystem to be processed should be unmounted or mounted
read-only.  The tool tries to check this before running, but you
should be careful.

%prep
%setup
%patch -p1
cp -p %SOURCE1 .
cp -p %SOURCE2 .

%build
export CFLAGS="%optflags"
make
gcc %optflags -o sparsify sparsify.c -lext2fs
docbook-to-man %SOURCE3 > zerofree.8

%install
install -pDm0755 zerofree %buildroot%_sbindir/zerofree
install -pDm0755 sparsify %buildroot%_sbindir/sparsify
install -Dm644 zerofree.8 %buildroot%_man8dir/zerofree.8

%files
%doc index.html
%_sbindir/zerofree
%_sbindir/sparsify
%_man8dir/zerofree.8*

%changelog
* Thu Aug 09 2012 Michael Shigorin <mike@altlinux.org> 1.0.2-alt1
- initial build for ALT Linux Sisyphus
  + spec based on fedora and opensuse packages
  + patch based on opensuse's one
  + manpage from debian

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu May 27 2010 Richard W.M. Jones <rjones@redhat.com> - 1.0.1-7
- Include zerofree(8) man page from Debian (RHBZ#596732).

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May 15 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.1-5
- Include the index file as a source file.
- Improve the description, remove spelling mistakes and other typos.
- Use the upstream SRPM directly, unpacking source from it.
- Fix use of dist macro.
- Pass the RPM OPTFLAGS to C compiler (should also fix debuginfo pkg).
- Use 'cp -p' to preserve timestamps when copying index.html file.
- Fix the defattr line.
- License is GPL+ (any version of the GPL including 1).
- Use a simpler install command to install the binary.
- Fix the upstream URL to point to the real original project.
- Add the sparsify command.

* Thu May 14 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.1-1
- Initial packaging for Fedora, based on R P Herrold's package.

* Wed May 13 2009 R P Herrold <info@owlriver.com> - 1.0.1-1
- initial packaging
