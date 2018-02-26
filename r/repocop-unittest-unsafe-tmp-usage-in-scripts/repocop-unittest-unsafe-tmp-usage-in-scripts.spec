%define testname unsafe-tmp-usage-in-scripts
Name: repocop-unittest-%testname
Version: 0.6
Release: alt3
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %testname integration tests for repocop test platform
Group: Development/Other
License: GPL or Artistic
Url: http://repocop.altlinux.org 
Requires: repocop

%description
%testname integration test for repocop test platform.
The test checks packages for unsafe /tmp usage.
The test is based on work of Dmitry E. Oboukhov <unera <at> debian.org>
(http://uvw.ru/find_the_bug2.sh) adapted for repocop.

%prep

%build
cat > %testname.whitelist <<'EOF'
installer-common-stage2
installer-feature-desktop-other-fs-stage2
installer-feature-services
lbuscd
make-initrd-propagator-resume
mkimage
mkimage-profiles
mkinitrd-initramfs
mod_security-doc
spt
spt-profiles-junior
bash-examples
python-module-pyinotify-examples
tcl-httpd-manual
EOF

cat > %testname.test <<'EOF'
#!/bin/sh

# based on work of Dmitry E. Oboukhov <unera <at> debian.org>
# http://uvw.ru/find_the_bug2.sh
# adapted for repocop by viy at altlinux.org

cwd=`pwd`
report_name="$REPOCOP_TEST_TMPDIR/report"
cat > $report_name <<'EOH'
The test discovered scripts with errors which may be used
by a user for damaging important system files.

For example if a script uses in its work a temp file which is created
in /tmp directory, then every user can create symlinks with the same
name (pattern) in this directory in order to destroy or rewrite some 
system or another user's files.

Scripts _must_ _use_ mktemp/tempfile or must use $TMPDIR.
mktemp/tempfile is safest. $TMPDIR is safer than /tmp/ 
because libpam-tmpdir creates a subdirectory of /tmp
that is only accessible by that user, and then sets TMPDIR and other
variables to that. Hence, it doesn't matter nearly as much if you
create a non-random filename, because nobody but you can access it.

EOH

cd $REPOCOP_PKG_ROOT
not_an_example_flag="$REPOCOP_TEST_TMPDIR/notanexample"
rm -f "$not_an_example_flag"
find . -type f -perm /111 | while read package_efile; do
        file $package_efile|grep -q script || continue
        if ! sed 's/#.*//' $package_efile|grep -q '/tmp/'; then
            continue
        fi

        file_found=''
        # checks
        sed 's/#.*//' $package_efile| \
            grep -q '>[[:space:]]*/tmp/' && file_found=1
        sed 's/#.*//' $package_efile| \
            grep -q 'tee[[:space:]][^|]*/tmp/' && file_found=1

        if test -z "$file_found"; then
            continue
        fi
        root_path_efile=`echo $package_efile|sed 's/^.//'`
        echo "Found error in $root_path_efile:" >> $report_name
        echo -e "\t\$ grep -A5 -B5 /tmp/ $root_path_efile" >> $report_name
        grep -A5 -B5 /tmp/ $package_efile|sed 's/^/\t/' >> $report_name
	case $root_path_efile in 
	     /usr/share/doc/*/examples/*) : ;;
	     *) touch "$not_an_example_flag" ;;
	esac
done
cd $cwd

if grep 'Found error' $report_name; then
    if grep '^'$REPOCOP_PKG_NAME'$' %_datadir/repocop/pkgtests/%testname/whitelist >/dev/null; then
        repocop-test-info `cat $report_name`
    elif [ -e "$not_an_example_flag" ]; then
        repocop-test-fail `cat $report_name`
    else
        repocop-test-info `cat $report_name`
    fi
else
    repocop-test-ok
fi
rm -f $report_name
EOF

%install
install -Dm 755 %testname.test %buildroot%_datadir/repocop/pkgtests/%testname/test
install -Dm 755 %testname.whitelist %buildroot%_datadir/repocop/pkgtests/%testname/whitelist

%files
#doc README ChangeLog
%_datadir/repocop/pkgtests/%testname

%changelog
* Thu Mar 22 2012 Igor Vlasenko <viy@altlinux.ru> 0.6-alt3
- added whitelist

* Tue Mar 31 2009 Igor Vlasenko <viy@altlinux.ru> 0.6-alt2
- added url

* Wed Dec 03 2008 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1
- really fixed bug: info instead of fail everywhere.

* Wed Dec 03 2008 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1
- fixed bug: info instead of fail everywhere.

* Sat Nov 15 2008 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1
- set to info level for /usr/share/doc/*/examples/*

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0.3-alt1
- another bugfix

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0.2-alt1
- fixed bugs in scripts

* Fri Sep 05 2008 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1
- First build for Sisyphus.
