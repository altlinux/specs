Name: nforenum
Version: 3.4.6
Release: alt1
Summary: NFORenum is a format correcter and linter for the NFO programming language.
Group: Development/Tools
License: GPLv2+
Url: http://users.tt-forums.net/dalestan/nforenum/
Source0: %name-%version-%release.tar
Patch0: %name-%version-%release.patch

# Automatically added by buildreq on Tue Sep 01 2009
BuildRequires: boost-devel gcc-c++

%description
NFORenum is a format correcter and linter for the NFO programming language. 

%prep
%setup -q -n %name-%version-%release
%patch0 -p 1

%build
%make

%install
for file in renum; do
  %__install -D -m 755 $file %buildroot%_bindir/$file
done


%files
%doc CHANGELOG.txt doc/*.en.txt
%_bindir/*

%changelog
* Tue Sep 01 2009 Anton Farygin <rider@altlinux.ru> 3.4.6-alt1
- first build for Sisyphus

