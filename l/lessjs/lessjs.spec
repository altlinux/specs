Name:		lessjs
Version:	1.3.1
Release:	alt2

Summary:	Less.js The dynamic stylesheet language

# cssmin.js is licensed under BSD license
# everything else is ASL 2.0
License:	ASL 2.0 and BSD

Group:		Development/Tools
URL:		http://lesscss.org

BuildArch:	noarch

Source0:	%name-%version.tar

# Disable YUI compression because lessjs otherwise
# would be carrying a bundled copy of cssmin.js
Patch0001:	0001-Disable-YUI-compression.patch

# Upstream version number is incorrect for 1.3.1
Patch0002:	0002-Fix-version-number.patch

# Use /usr/share paths instead of /usr/lib
Patch0003:	0003-substitute-paths-to-use-usr-share-instead-of-usr-lib.patch

# Remove pre-built files from the dist/ directory
Patch0004:	0004-Remove-pre-builds.patch

BuildRequires:	node
Requires:	node

%description
LESS extends CSS with dynamic behavior such as variables, mixins,
operations and functions. LESS runs on both the client-side (Chrome,
Safari, Firefox) and server-side, with Node.js and Rhino.

%prep
%setup

%patch0001 -p1
%patch0002 -p1
%patch0003 -p1
%patch0004 -p1

%build
# Nothing to be built, we're just carrying around flat files

%check
make %{?_smp_mflags} test

%install
mkdir -p %buildroot%_bindir/
install bin/lessc %buildroot%_bindir/
mkdir -p %buildroot%_datadir/less/
cp -rp lib/less %buildroot%_datadir/

%files
%doc LICENSE README.md
%_bindir/lessc
%_datadir/less/

%changelog
* Mon Aug 26 2013 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt2
- cleanup spec

* Mon Jul 15 2013 Pavel Shilovsky <piastry@altlinux.org> 1.3.1-alt1
- Initial release for Sisyphus (based on Fedora)
