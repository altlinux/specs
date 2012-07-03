%define testname buildroot

Name: repocop-unittest-%testname
Version: 0.07
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %testname integration tests for repocop test platform
Group: Development/Other
License: GPL or Artistic
Url: http://repocop.altlinux.org 
Requires: repocop

%description
%testname integration test for repocop test platform.
The test finds packages that contains a piece of path
to buildroot where they were built.
It often indicates an essential bug in the package
such as misconfiguration.

%prep

%build
cat > test <<'EOF'
#!/bin/bash
# we have no $REPOCOP_PKG_SRC_NAME yet, so try to guess it from the source rpm string
srcname=
if [ "${REPOCOP_PKG_SOURCEPKG%%-$REPOCOP_PKG_RELEASE}" != "$REPOCOP_PKG_SOURCEPKG" ]; then
    srcname=${REPOCOP_PKG_SOURCEPKG%%-$REPOCOP_PKG_RELEASE}
    if [ "${srcname%%-$REPOCOP_PKG_VERSION}" != "$srcname" ]; then
        srcname=${srcname%%-$REPOCOP_PKG_VERSION}
    else
        srcname=${srcname%%[-0-9.]*}
    fi
fi
################
STATUS=ok
declare -a MESSAGE
i=0
for file in `grep -s -r -l $srcname-buildroot $REPOCOP_PKG_ROOT/`; do
    filename=`echo $file | sed -e "s,$REPOCOP_PKG_ROOT,,g"`
    case $file in
	*.elc|*.pyc|*/environment.pickle) : exclude them ;;
	*)
        [ "$STATUS" = "fail" ] || MESSAGE[i++]="found paths to buildroot: "
    	STATUS=fail
	MESSAGE[i++]="$filename: "`grep -s $srcname-buildroot $file | sed -e "s,$REPOCOP_PKG_ROOT,,g"`
	;;
    esac
done
exec repocop-test-$STATUS "${MESSAGE[@]}"
EOF

cat > description <<'EOF'
The test finds packages that contains a piece of path
to buildroot where they were built.
It often indicates an essential bug in the package
such as misconfiguration.
TODO: write page on wiki.
EOF

%install
mkdir -p $RPM_BUILD_ROOT%_datadir/repocop/pkgtests/%testname/
%__install -m 755 test $RPM_BUILD_ROOT%_datadir/repocop/pkgtests/%testname/
%__install -m 644 description $RPM_BUILD_ROOT%_datadir/repocop/pkgtests/%testname/

%files
#doc README ChangeLog
%_datadir/repocop/pkgtests/%testname

%changelog
* Thu Aug 19 2010 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- more readable output

* Thu Aug 19 2010 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- excluded *.pyc|*/environment.pickle files

* Wed Aug 18 2010 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- fixed bug in test

* Tue Mar 31 2009 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2
- added url

* Fri Mar 07 2008 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- fixed bug in source name heuristic

* Thu Mar 06 2008 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- search for source name (thanks to damir@).

* Sat Mar 01 2008 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- First build for Sisyphus.
