# revision 15878
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-pdfwin
Version:	20111103
Release:	1
Summary:	TeXLive pdfwin package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfwin.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfwin.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
TeXLive pdfwin package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pdfwin/pdfwin.cfg
%{_texmfdistdir}/tex/latex/pdfwin/pdfwin.sty
%doc %{_texmfdistdir}/doc/latex/pdfwin/BucResampling.pdf
%doc %{_texmfdistdir}/doc/latex/pdfwin/BucSystem1.pdf
%doc %{_texmfdistdir}/doc/latex/pdfwin/BucSystem2.pdf
%doc %{_texmfdistdir}/doc/latex/pdfwin/BucSystem3.pdf
%doc %{_texmfdistdir}/doc/latex/pdfwin/BucSystem4.pdf
%doc %{_texmfdistdir}/doc/latex/pdfwin/BucSystem5.pdf
%doc %{_texmfdistdir}/doc/latex/pdfwin/BucSystem6.pdf
%doc %{_texmfdistdir}/doc/latex/pdfwin/Bucuresti2003.tex
%doc %{_texmfdistdir}/doc/latex/pdfwin/JWGU-Logo.png
%doc %{_texmfdistdir}/doc/latex/pdfwin/Thumbs.db
%doc %{_texmfdistdir}/doc/latex/pdfwin/marble.png
%doc %{_texmfdistdir}/doc/latex/pdfwin/normprot.tex
%doc %{_texmfdistdir}/doc/latex/pdfwin/shortvec.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
