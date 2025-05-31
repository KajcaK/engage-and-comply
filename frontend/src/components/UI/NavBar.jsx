import {Container, Nav, Navbar} from "react-bootstrap";

const NavBar = () => (
    <Navbar expand="lg" bg="dark" variant="dark" className="navbar-container">
        <Container fluid>
            <Navbar.Brand href="/" className="d-flex align-items-center text-white text-decoration-none fs-4 ms-3">
                A.C.E. - AI for Compliant Engagement
            </Navbar.Brand>
            <Navbar.Toggle aria-controls="app-navbar"/>
            <Navbar.Collapse id="app-navbar" className="bg-dark navbar-collapse">
                <Nav className="ms-auto me-5 my-2 justify-content-center align-items-center">
                    <Nav.Link href="/" className="me-1">Chat</Nav.Link>
                    <Nav.Link href="/upload-link">Upload Link</Nav.Link>
                    <Nav.Link href="/upload-pdf">Upload PDF</Nav.Link>
                </Nav>
            </Navbar.Collapse>
        </Container>
    </Navbar>
);

export default NavBar