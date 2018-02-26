# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/dvipdf /usr/bin/dvips gcc-c++
# END SourceDeps(oneline)
Summary:	      2D Quantum Monte Carlo simulator for semiconductor devices
Name:		      archimedes
Version:	      2.0.0
Release:	      alt2_2
License:	      GPLv3+
Group:		   Engineering
URL:		      http://www.gnu.org/software/archimedes/
Source0:	      ftp://ftp.gnu.org/gnu/archimedes/%{name}-%{version}.tar.gz


BuildRequires:	dos2unix
BuildRequires:	ghostscript-utils ghostscript
BuildRequires:	/usr/bin/latex texlive-latex-recommended
Source44: import.info

%description
Archimedes is a package for the design and simulation of submicron
semiconductor devices. It is a 2D Fast Monte Carlo simulator which can take
into account all the relevant quantum effects, thank to the implementation of
the Bohm effective potential method.

The physics and geometry of a general device is introduced by typing a simple
script, which makes, in this sense, Archimedes a powerful tool for the
simulation of quite general semiconductor devices.

%prep
%setup -q

# Suppress rpmlint error.
dos2unix COPYING

# Use tests as user examples
cp -pr tests/ examples/

%build
%configure --enable-manual
make %{?_smp_mflags}

%install

make install INSTALL="%{__install} -p" DESTDIR=$RPM_BUILD_ROOT

# We don't want 3 documents to explain the same thing
rm -f ${buildroot}%{_docdir}/%{name}.{dvi,ps}

%files
%doc AUTHORS
%doc ChangeLog
%doc COPYING
%doc NEWS
%doc README
%doc THANKS
%doc doc/%{name}.pdf
%doc examples/
%{_bindir}/%{name}

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt2_2
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_2
- update to new release by fcimport

* Sat Dec 10 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_1
- update to new release by fcimport

* Fri Jul 15 2011 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt1_2
- initial release by fcimport

