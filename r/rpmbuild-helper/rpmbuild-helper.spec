Name: rpmbuild-helper
Version: 0.06
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: A set of helper utilities that automate routine packaging tasks.
Group: Development/Tools
License: GPL or Artistic
Url: http://www.altlinux.org/Icon_Paths_Policy

Source: %name-%version.tar

%description
A set of helper utilities that automate routine packaging tasks.


%package desktop
Group: Development/Tools
Summary: A tool for auto repairing .desktop files in rpm packages
Requires: rpm-build > 4.0.4-alt100.56

%description desktop
A tool for auto repairing .desktop files in rpm packages.
A part of rpmbuild-helper utilities.

%package sugar-activity
Group: Development/Tools
Summary: A tool for auto repairing activity.info files in rpm packaged sugar activities
Requires: rpm-build > 4.0.4-alt100.56

%description sugar-activity
A tool for auto repairing activity.info files in rpm packaged sugar activities.
A part of rpmbuild-helper utilities.

%package iconsdir
Group: Development/Tools
Summary: A tool for auto creating missing pixmaps in rpm packages
Requires: rpm-build > 4.0.4-alt100.56
Requires: /usr/bin/convert

%description iconsdir
A tool for auto creating missing pixmaps in rpm packages.
A part of rpmbuild-helper utilities.

%prep
%setup

%build
#perl_vendor_build

cat > ./025-fixup-iconsdir.brp <<'EOF'
#!/usr/bin/perl -w
use File::Basename;
use strict;
die '$RPM_BUILD_ROOT is not set!' unless $ENV{'RPM_BUILD_ROOT'};
`mkdir -p $ENV{'RPM_BUILD_ROOT'}%_liconsdir`;

my $outfile;

sub convert_to {
    my ($infile, $outfile, $geometry) =@_;
    unless (-e $outfile) {
    	print STDERR "025-fixup-iconsdir: converted ".&basename($infile)." to $geometry\n";
        system ("convert $infile -resize $geometry $outfile") and die $!;
    }
}
# TODO: check size instead of converting
foreach my $pixmapfile (glob $ENV{'RPM_BUILD_ROOT'}.'/usr/share/pixmaps/*.*') {
	my $filename=basename($pixmapfile);
	&convert_to($pixmapfile, $ENV{'RPM_BUILD_ROOT'}.'%_liconsdir/'.$filename, 48);
}
EOF

%install
mkdir -p $RPM_BUILD_ROOT%_prefix/lib/rpm/brp.d/
install -m 755 *-fixup-*.brp $RPM_BUILD_ROOT%_prefix/lib/rpm/brp.d/

# not ready
rm -f $RPM_BUILD_ROOT%_prefix/lib/rpm/brp.d/025-fixup-iconsdir.brp
#%files iconsdir
#%_prefix/lib/rpm/brp.d/025-fixup-iconsdir.brp

%files desktop
%_prefix/lib/rpm/brp.d/025-fixup-desktop.brp

%files sugar-activity
%_prefix/lib/rpm/brp.d/025-fixup-sugar-activity.brp

%changelog
* Sun Dec 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- bugfix release

* Sun Dec 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- updated for modular rpm-build
- added 025-fixup-sugar-activity

* Sat Dec 08 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- updated to rev.3 of Icon Paths Policy

* Thu Nov 06 2008 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- verbose output in rpmbuild-helper-desktop
- two more fixes for .desktop files

* Wed Nov 05 2008 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- fix in rpmbuild-helper-desktop (thanks to ildar@)

* Mon Nov 03 2008 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- first build

