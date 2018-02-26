Name: rpmbuild-helper
Version: 0.03
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: A set of helper utilities that automate routine packaging tasks.
Group: Development/Tools
License: GPL or Artistic
#Url: 

Source: %name-%version.tar

#BuildRequires: perl-RPM-Source-Editor
#Requires: perl-RPM perl-DBD-SQLite sqlite3

%description
A set of helper utilities that automate routine packaging tasks.


%package desktop
Group: Development/Tools
Summary: tool for auto repairing .desktop files in rpm packages
Requires: %name = %version-%release

%description desktop
A tool for auto repairing .desktop files in rpm packages.
A part of rpmbuild-helper utilities.

%package iconsdir
Group: Development/Tools
Summary: tool for auto creating missing pixmaps in rpm packages
Requires: %name = %version-%release
Requires: ImageMagick

%description iconsdir
A tool for auto creating missing pixmaps in rpm packages.
A part of rpmbuild-helper utilities.

%prep
%setup

%build
#perl_vendor_build

cat > ./rpmbuild-helper-iconsdir <<'EOF'
#!/usr/bin/perl -w
use File::Basename;
use strict;
die '$RPM_BUILD_ROOT is not set!' unless $ENV{'RPM_BUILD_ROOT'};
`mkdir -p $ENV{'RPM_BUILD_ROOT'}%_miconsdir`;
`mkdir -p $ENV{'RPM_BUILD_ROOT'}%_niconsdir`;
`mkdir -p $ENV{'RPM_BUILD_ROOT'}%_liconsdir`;

my $outfile;

sub convert_to {
    my ($infile, $outfile, $geometry) =@_;
    unless (-e $outfile) {
    	print STDERR "rpmbuild-helper-iconsdir: converted ".&basename($infile)." to $geometry\n";
        system ("convert $infile -resize $geometry $outfile") and die $!;
    }
}

foreach my $pixmapfile (glob $ENV{'RPM_BUILD_ROOT'}.'%_liconsdir/*.*') {
	my $filename=basename($pixmapfile);
	&convert_to($pixmapfile, $ENV{'RPM_BUILD_ROOT'}.'%_niconsdir/'.$filename, 32);
	&convert_to($pixmapfile, $ENV{'RPM_BUILD_ROOT'}.'%_miconsdir/'.$filename, 16);
}
foreach my $pixmapfile (glob $ENV{'RPM_BUILD_ROOT'}.'/usr/share/pixmaps/*.*') {
	my $filename=basename($pixmapfile);
	&convert_to($pixmapfile, $ENV{'RPM_BUILD_ROOT'}.'%_liconsdir/'.$filename, 48);
	&convert_to($pixmapfile, $ENV{'RPM_BUILD_ROOT'}.'%_niconsdir/'.$filename, 32);
	&convert_to($pixmapfile, $ENV{'RPM_BUILD_ROOT'}.'%_miconsdir/'.$filename, 16);
}
EOF
%install
#perl_vendor_install

mkdir -p $RPM_BUILD_ROOT%_bindir
install -m 755 rpmbuild-helper rpmbuild-helper-* $RPM_BUILD_ROOT%_bindir/

%files
%_bindir/rpmbuild-helper
#%_man1dir/repocop-*
#%perl_vendor_privlib/T*
#%perl_vendor_man3dir/*

%files desktop
%_bindir/rpmbuild-helper-desktop

%files iconsdir
%_bindir/rpmbuild-helper-iconsdir

%changelog
* Thu Nov 06 2008 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- verbose output in rpmbuild-helper-desktop
- two more fixes for .desktop files

* Wed Nov 05 2008 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- fix in rpmbuild-helper-desktop (thanks to ildar@)

* Mon Nov 03 2008 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- first build

