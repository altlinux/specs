BuildRequires: texlive-latex-extra
Name:		E
Version:	1.5
Release:	alt1_1
Summary:	Equational Theorem Prover
Group:		Engineering
License:	GPLv2+ or LGPLv2+
URL:		http://www.eprover.org/
Source0:	http://www4.in.tum.de/~schulz/WORK/E_DOWNLOAD/V_%{version}/%{name}.tgz
# Sent upstream 7 May 2012.  Use a union to avoid a violation of ANSI C
# aliasing rules.
Patch0:         %{name}-alias.patch

# Building actually checks for specific versions of python; building may
# need to be updated for new versions of python 2:
BuildRequires:  help2man
BuildRequires:	/usr/bin/latex texlive-latex-recommended
Source44: import.info
# You can verify the CASC results here: http://www.cs.miami.edu/~tptp/CASC/J4/

%description
E is a purely equational theorem prover for full first-order logic.
That means it is a program that you can stuff a mathematical
specification (in first-order format) and a hypothesis into, and which
will then run forever, using up all of your machines' resources.  Very
occasionally it will find a proof for the hypothesis and tell you so.

E's inference core is based on a modified version of the superposition
calculus for equational clausal logic.  Both clausification and
reasoning on the clausal form can be documented in checkable proof
objects.

E was the best-performing open source software prover in the 2008 CADE
ATP System Competition (CASC) in the FOF, CNF, and UEQ divisions.  In
the 2011 competition, it won second place in the FOF division, and
placed highly in CNF and UEQ.

%prep
%setup -q -n E
%patch0

# Set up Fedora CFLAGS and paths
sed -e "s|^EXECPATH = .*|EXECPATH = $RPM_BUILD_ROOT%{_bindir}|" \
    -e "s|^MANPATH = .*|MANPATH = $RPM_BUILD_ROOT%{_mandir}/man1|" \
    -e "s|^CFLAGS.*|CFLAGS = $RPM_OPT_FLAGS -std=gnu99 \\\\|" \
    -i Makefile.vars
sed -i "s|^EXECPATH=.*|EXECPATH=%{_bindir}|" PROVER/eproof PROVER/eproof_ram

# Fix the character encoding of one file
iconv -f ISO8859-1 -t UTF-8 DOC/E-REMARKS > DOC/E-REMARKS.utf8
touch -r DOC/E-REMARKS DOC/E-REMARKS.utf8
mv -f DOC/E-REMARKS.utf8 DOC/E-REMARKS

# Preserve timestamps when installing
sed -i 's|cp \$1|cp -p $1|' development_tools/e_install

find */ -name Makefile -exec sed -i -e 's/^\(\t$(LD).*\)/\1 $(LIBS)/' {} \;


%build
# smp_mflags causes unwelcome races, so we will not use it
make remake
make man

%install
make install

%check
./PROVER/eprover -s --tptp-in EXAMPLE_PROBLEMS/TPTP/SYN310-1+rm_eq_rstfp.tptp | tail -1 > test-results
echo "# SZS status Unsatisfiable" > test-expected-results
diff test-results test-expected-results


%files
%doc README
%doc COPYING
%doc DOC/bug_reporting
%doc DOC/clib.ps
%doc DOC/CREDITS
%doc DOC/E-1.4pre.html
%doc DOC/eprover.pdf
%doc DOC/E-REMARKS
%doc DOC/E-REMARKS.english
%doc DOC/grammar.txt
%doc DOC/NEWS
%doc DOC/sample_proofs.html
%doc DOC/sample_proofs_tstp.html
%doc DOC/TODO
%doc DOC/TSTP_Syntax.txt
%doc DOC/WISHLIST
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Fri May 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_1
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2_3
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_3
- update to new release by fcimport

* Wed Jan 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_2
- update to new release by fcimport

* Fri Aug 26 2011 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_1
- update to new release by fcimport

* Fri Jul 15 2011 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_1
- update to new release by fcimport

* Thu Jun 09 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.002-alt1_6
- converted from Fedora by srpmconvert script

