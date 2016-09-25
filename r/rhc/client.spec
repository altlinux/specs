Summary:       Multi-tenant cloud management system client tools
Name:          rhc
Version:       1.38.6
Release:       alt1
Group:         System/Servers
License:       ASL 2.0
URL:           http://openshift.redhat.com
Source0:       rhc-%version.tar
Patch0:        rhc-%version-%release.patch

BuildArch:     noarch

BuildRequires: rpm-build-ruby
Requires:      git ruby-parseconfig ruby-json

Obsoletes:     ruby-rhc-rest

%def_without doc

%if_with doc
BuildRequires: ruby-tool-rdoc
%endif

%description
Provides OpenShift client libraries

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

%prep
%setup -q
%patch -p1

%build
for f in bin/rhc
do
  ruby -c $f
done

for f in lib/*.rb
do
  ruby -c $f
done

%install
mkdir -p %buildroot%_man1dir
mkdir -p %buildroot%_man5dir

for f in man/*
do
  len=`expr length $f`
  section=`expr substr $f $len $len`
  cp $f "%buildroot/usr/share/man/man$section/"
done

mkdir -p %buildroot%_sysconfdir/openshift
cp conf/express.conf %buildroot%_sysconfdir/openshift/

mkdir -p %buildroot%_bindir
cp bin/* %buildroot%_bindir/

mkdir -p %buildroot%ruby_sitelibdir
cp -a lib/* %buildroot%ruby_sitelibdir/

# Copy the bash autocompletion script
mkdir -p %buildroot%_sysconfdir/bash_completion.d
cp autocomplete/rhc_bash %buildroot%_sysconfdir/bash_completion.d/rhc

%if_with doc
%rdoc lib/
%endif

%files
%doc LICENSE COPYRIGHT
%_bindir/rhc*
%_man1dir/rhc*
%_man5dir/express*
%ruby_sitelibdir/*
%config(noreplace) %_sysconfdir/openshift/express.conf
%_sysconfdir/bash_completion.d/rhc

%if_with doc
%files doc
%ruby_ri_sitedir/RHC*
%endif

%changelog
* Sun Sep 25 2016 Evgeny Sinelnikov <sin@altlinux.ru> 1.38.6-alt1
- update to last release

* Tue Aug 13 2013 Evgeny Sinelnikov <sin@altlinux.ru> 1.13.1-alt1
- Update for new release

* Mon Aug 12 2013 Evgeny Sinelnikov <sin@altlinux.ru> 1.4.1-alt1
- Update to last used release

* Sat Dec 01 2012 Led <led@altlinux.ru> 0.96.2-alt2.1
- Rebuilt with ruby-1.9.3-alt1
- cleaned up BuildRequires

* Wed Aug 01 2012 Evgeny Sinelnikov <sin@altlinux.ru> 0.96.2-alt2
- Fix obsoletes of ruby-rhc-rest

* Wed Aug 01 2012 Evgeny Sinelnikov <sin@altlinux.ru> 0.96.2-alt1
- Update for new release
- Add bash autocompletion support
- Obsolete rhc-rest package due includes it

* Fri Apr 13 2012 Evgeny Sinelnikov <sin@altlinux.ru> 0.90.4-alt1
- Update for new release

* Wed Jan 18 2012 Evgeny Sinelnikov <sin@altlinux.ru> 0.85.1-alt1
- Update for new release
- Fix some compatibility problems with ruby-1.9

* Fri Dec 16 2011 Evgeny Sinelnikov <sin@altlinux.ru> 0.84.2-alt1
- Initial build for ALT Linux Sisyphus

